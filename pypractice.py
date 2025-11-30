# %%
import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import torch.cuda
import torch
print(torch.cuda.is_available())
print(torch.cuda.get_device_name(0))
device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
X = pd.read_pickle(f"./input.pkl")
y = pd.read_pickle(f"./output.pkl")
newdf=pd.concat([X,y],axis=1)
col_minmax = {
    idx: (newdf.iloc[:, idx].min(), newdf.iloc[:, idx].max())
    for idx in range(newdf.shape[1])
}


import os
os.environ["CUDA_LAUNCH_BLOCKING"] = "1"
os.environ["CUDA_VISIBLE_DEVICES"] = ""



# %%
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import TensorDataset, DataLoader,Subset
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix


# 머신러닝 관련 라이브러리
from sklearn.metrics import classification_report, confusion_matrix

#기억력 관련 변수 ->cerad 4,6,7,8(8,10,11,12)
#사고력 관련 변수 ->cerad 1,2,3,5,9,10,11,12 (5,6,7,9,13,14,15,16)
# 나머지 변수 -> age,gender, edu,s_adl,s_iadl  (0,1,2,3,4)
# 범주형 파생변수 -> j1v, 2,5,6,9,10,11,adl,iadl


def to_tensor(*dfs):
    return [torch.tensor(df.values,dtype=torch.float32) for df in dfs]



class MainModule(nn.Module):
    def __init__(self,input_dim=6,output_dim=3,do1=0.5,activ=0):
        super().__init__()
        self.activ=nn.GELU() if activ==1 else nn.ReLU()
        self.input_layer=nn.Sequential(
            nn.Linear(input_dim,6),
            self.activ,
            nn.Dropout(do1),
            
            nn.Linear(6,4),
            self.activ,
            nn.Dropout(do1),

            nn.Linear(4,3),
            self.activ,
            nn.Dropout(do1),
        )
        
        self.output_layer=nn.Linear(3,output_dim)
    def forward(self,x):
        x=self.input_layer(x)
        output=self.output_layer(x)
        return output

class SubModule(nn.Module):
    def __init__(self,input_dim=28,output_dim=7,do1=0.5,activ=0):
        super().__init__()
        self.activ=nn.GELU() if activ==1 else nn.ReLU()
        self.input_layer=nn.Sequential(
            nn.Linear(input_dim,28),
            self.activ,
            nn.Dropout(do1),
            
            nn.Linear(28,14),
            self.activ,
            nn.Dropout(do1),

            nn.Linear(14,7),
            self.activ,
            nn.Dropout(do1),
        )
        
        self.output_layer=nn.Linear(7,output_dim)
    def forward(self,x):
        x=self.input_layer(x)
        output=self.output_layer(x)
        return output

class TotalModel(nn.Module):    #TotalModel의 128 dim에서 skip connection 적용
    def __init__(self,do1,do2,activ):
        super().__init__()

        self.activ=nn.GELU() if activ==1 else nn.ReLU()

        self.module1=SubModule(6,3,do1,activ)
        self.module2=SubModule(28,7,do1,activ)

        
        self.hidden_layers=nn.ModuleList([
            nn.Sequential(
                nn.Linear(10,10),
                self.activ,
                nn.Dropout(do2),
            )for _ in range(1)
        ])
        
        self.output_layers=nn.Sequential(
            nn.Linear(10,5),
            self.activ,
            nn.Dropout(do2),
            
            nn.Linear(5,5),
            self.activ,
            nn.Dropout(do2),            
            
            nn.Linear(5,3)         
        )
        
    
    def forward(self,x):
        x1=x[:,[0,1,2,4,28,31]]
        x2=x[:,[3,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,29,30,32,33]]

        out1=self.module1(x1)        #특정 4개의 열 데이터는 module1에 통과 -> output1 나온다      -shape:[batch_size,16]
        out2=self.module2(x2)        #나머지 13개의 열 데이터는 module2에 통과 -> output2 나온다   -shape:[batch_size,16]

        out=torch.cat([out1,out2],dim=1)       #-shape:[batch_size,32]
        k=out
        residual=k          #초기 결과를 k로 잔차 저장
        for layer in self.hidden_layers:
            j=layer(k)
            k=j+residual
            
        output=self.output_layers(k)
        return output
        


# %%
class PatientEnv:
    def __init__(self, patient_data, score_model, max_steps=5):
        """
        patient_data: dict {patient_id: {"features": np.array, "label": int}}
        score_model: scoring DNN 모델 (reward용)
        """
        self.state = np.zeros(34, dtype=np.float32)        
        self.patient_data = patient_data
        self.score_model = score_model
        self.max_steps = max_steps
        self.num_features = list(patient_data.values())[0]['features'].shape[0]

    def reset(self, patient_id):  #pid를 받고 해당 환자의 변수정보를 state에 저장
        self.patient = self.patient_data[patient_id]
        self.state = self.patient['features'].copy()
        self.steps = 0
        self.done = False
        return self.state.copy()
    def reset_from_dict(self, input_dict):
        feature_names = [
    'gender','age','race','educ','marry','house','pov','wt','ht','bmi','wst','hip',
    'dia','pulse','sys','alt','albumin','ast','crea','chol','tyg','ggt','wbc','hb',
    'hct','ldl','hdl','acratio','glu','insulin','crp','hb1ac','mvpa','ac_week'
]


        # 환경용 feature 순서에 맞게 value 배열 생성
        state_list = []
        for key in feature_names:
            if key not in input_dict:
                raise KeyError(f"{key} is missing in input_dict")
            state_list.append(float(input_dict[key]))

        # numpy state 저장
        self.state = np.array(state_list, dtype=np.float32)
        self.steps = 0
        self.done = False
        return self.state.copy()


    def step(self, action_idx, delta, alpha=100):
        """
        action: [action_idx; 선택할 변수 인덱스 , delta; idx 변수에 대해서 변화시킬 값의 정도] 
        delta: float, 선택 변수에 더할 값
        """

        # 변수별 min-max 범위 적용
        var_min, var_max =col_minmax[action_idx.item()]  # 필요하면 실제 min-max 값 사용

        # reward 계산: scoring model 통과
        old_state_tensor = torch.tensor(self.state, dtype=torch.float32).unsqueeze(0)
        with torch.no_grad():
            old_reward = self.score_model(old_state_tensor)  #이전 시기의 state -> reward계산
        
        
        self.state[action_idx.item()]= np.clip(self.state[action_idx.item()]+ delta.item(), var_min, var_max)  # action으로 state update

        new_state_tensor = torch.tensor(self.state, dtype=torch.float32).unsqueeze(0)  #new state -> reward계산
        with torch.no_grad():
            new_reward = self.score_model(new_state_tensor)

        self.steps += 1
        self.done = self.steps >= self.max_steps
        return self.state.copy(), alpha*(old_reward-new_reward), self.done   #업데이트된 state 반환, dbs score의 감소량에 비례하는 보상 -> dbs score감소를 촉진, episode 끝났는지 반환

    def state_dim(self):
        return self.num_features

    def action_dim(self):
        return self.num_features  # 34개 변수 중 1개 선택

# %%
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical

class HybridActor(nn.Module):
    def __init__(self, state_dim=34, discrete_dim=34):
        super().__init__()
        self.state_dim = state_dim
        self.discrete_dim = discrete_dim

        # Shared encoder
        self.shared = nn.Sequential(
            nn.Linear(state_dim, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU()
        )

        # Discrete head (variable index 선택)
        self.discrete_head = nn.Linear(64, discrete_dim)
        

        # Delta head: state + one-hot(index) 입력
        # input dim = state_dim + discrete_dim
        self.delta_net = nn.Sequential(
            nn.Linear(state_dim + discrete_dim, 128),
            nn.ReLU(),
            nn.Linear(128, 40),
            nn.ReLU(),
            nn.Linear(40, 8),
            nn.ReLU(),
            nn.Linear(8, 4),
            nn.ReLU(),
            nn.Linear(4, 1),
        )

    def forward(self, state):
        h = self.shared(state)
        logits = self.discrete_head(h)
        dist = Categorical(logits=logits) 
        action_index = dist.sample()   #34개의 변수에 대한 logit값을 얻은 후에, 이 logit으로 dist 만들어서 index 정수값 샘플링한다. (후반에 별로 -> epsilon-greedy?)
        return action_index

    def compute_delta(self, state, action_index):
        if state.dim() == 1:
            state = state.unsqueeze(0)  # [1, state_dim]

        # action_index도 1차원으로 맞춤
        if action_index.dim() == 0:   # 스칼라
            action_index = action_index.unsqueeze(0)  # [1]
        # One-hot 인코딩
        onehot = F.one_hot(action_index.long(), num_classes=self.discrete_dim).float()

        # concat
        x = torch.cat([state, onehot], dim=1)

        # delta 예측
        delta = self.delta_net(x)
        var_min, var_max =col_minmax[action_index.item()]
        delta = torch.clamp(delta, min=var_min, max=var_max)
        return delta
    
def load_best_model(model, device=device):
    model = model.to(device)
    model.load_state_dict(torch.load("model/best_model.pt", map_location=device))
    model.eval()
    return model

def scoring(state_input):
    
    X_patient_t = state_input.float()
    if X_patient_t.ndim == 1:
        X_patient_t = X_patient_t.unsqueeze(0) 

    # 모델 불러오기
    model = load_best_model(TotalModel(0.35, 0.35, 1))
    model.eval()
    
    with torch.no_grad():
        output = model(X_patient_t.to(device))   # [1, 3]
        prob = torch.softmax(output, dim=1)      # [1,3]
        prob = prob.squeeze(0)                    # [3]

    # scoring 계산
    score = (prob[1].item() + prob[2].item() * 2) * 50
    return score

# %%
def test_patient(env, actor, patient_dict, max_steps=8):
    feature_names = [
        'gender','age','race','educ','marry','house','pov','wt','ht',
        'bmi','wst','hip','dia','pulse','sys','alt','albumin','ast',
        'crea','chol','tyg','ggt','wbc','hb','hct','ldl','hdl',
        'acratio','glu','insulin','crp','hb1ac','mvpa','ac_week'
    ]

    # state 만들기
    state = np.array([patient_dict[f] for f in feature_names], dtype=np.float32)

    # 결과 dict 초기화
    output_dict = dict(patient_dict)

    old_score = scoring(torch.tensor(state, dtype=torch.float32))


    done = False
    for step in range(1, max_steps + 1):

        state_tensor = torch.tensor(state, dtype=torch.float32)

        # --- action 선택 ---
        action_idx = actor(state_tensor)
        delta = actor.compute_delta(state_tensor, action_idx)
        delta_float=delta.item()

        # === ENV STEP ===
        next_state, reward, done = env.step(action_idx, delta, alpha=5)

        # step 기록
        feature_name = feature_names[int(action_idx.item())]
        output_dict[f"{step}week"] = (feature_name, delta_float)

        state = next_state
        new_score = scoring(torch.tensor(state, dtype=torch.float32))



    output_dict["old_score"] = old_score
    output_dict["new_score"] = new_score

    return output_dict


# %%
# run_eval.py

input_dict = {'gender': 1.0, 'age': 33.0, 'race': 1.0, 'educ': 4.0, 'marry': 1.0, 'house': 2.0, 'pov': 3.28, 'wt': 113.8, 
                'ht': 178.5, 'bmi': 35.7, 'wst': 121.8, 'hip': 113.3, 'dia': 79.0, 'pulse': 73.0, 'sys': 114.0, 'alt': 62.0, 'albumin': 4.0, 
                'ast': 32.0, 'crea': 0.82, 'chol': 170.0, 'tyg': 168.0, 'ggt': 36.0, 'wbc': 6.7, 'hb': 15.5, 'hct': 46.3, 'ldl': 106.0, 
                'hdl': 33.0, 'acratio': 5.24, 'glu': 204.0, 'insulin': 22.77, 'crp': 8.81, 'hb1ac': 9.5, 'mvpa': 840.0, 'ac_week': 0.173077, 
                'context':"dd"}
patient_data = {
    i: {"features": X.iloc[i], "label": y.iloc[i]} for i in range(newdf.shape[0])
}

env = PatientEnv(patient_data, scoring, max_steps=8)
env.reset_from_dict(input_dict)

# 2) actor 모델 로드
actor = HybridActor()
actor.load_state_dict(torch.load("model/actor.pt"))
actor.eval()

# 3) 평가 실행
rl_output = test_patient(env, actor, input_dict)
print(rl_output)


# %%
from main import llm
result=llm(rl_output)
print(result)
print("dd")

