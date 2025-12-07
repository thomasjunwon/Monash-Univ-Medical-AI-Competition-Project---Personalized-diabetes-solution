import streamlit as st
from input_widgets import numeric_input
import pandas as pd
from patient_demo import DEMO_FEATURES

st.set_page_config(page_title="Diabetes Risk Tool", layout="wide")

# --------------------
# 0. 추천 텍스트를 만드는 함수
# --------------------
def get_recommendation(features: dict) -> str:
    """
    Demo 모드일 때는 고정 텍스트,
    일반 모드일 때는 나중에 친구 모델(LLM/백엔드)에서 받아온 텍스트를 리턴하는 자리.
    """
    # 🔹 Demo 모드: 항상 같은 텍스트 리턴
    if st.session_state.get("demo_mode", False):
        return (
"Initial Score: 99.9832\n"

"====================\n"


"Final Score: 95.7315\n"

"====================\n"


"FINAL RECOMMENDATION\n"
"====================\n"
"\n"
"1. Working on mvpa (moderate to vigorous physical activity): from 40 to 60 minutes per week\n"
"- What this step means: You are aiming to increase your weekly active time by 20 minutes, going from 40 to 60 minutes of moderate to vigorous activity each week.\n"
"- Why this helps your health: Moving more can help your body use sugar better and support your heart and blood vessels. It can also help with weight and energy.\n"
"- A realistic plan for you: I know your knee pain and shift work make exercise tough. Try walking gently for 10 minutes after your shift, maybe around your home or a nearby park. On days off, you could do 2 sets of 10 chair sit-to-stands to build strength without hurting your knees. Also, try stretching or gentle yoga at home to keep moving without strain.\n"
"- How this fits ADA guidelines: This matches ADA advice to increase physical activity safely to help your diabetes and overall health.\n"
"\n"
"2. Working on ac_week (activity sessions per week): from 0 to 1 session per week\n"
"- What this step means: You are starting to add at least one session of physical activity each week, moving from no sessions to one session weekly.\n"
"- Why this helps your health: Regular activity helps your body manage blood sugar and can lower risks of complications. Even one session a week is a good start.\n"
"- A realistic plan for you: With your busy schedule and knee discomfort, start small. Pick one day each week to do a 15-minute walk or gentle exercise like swimming if available. You can do this at a time that fits your shift, maybe right after work or before your shift starts.\n"
"- How this fits ADA guidelines: This fits ADA guidance encouraging regular physical activity spread throughout the week.\n"
"\n"
"3. Working on sugary_drinks_per_day: decrease by 0.5 servings per day\n"
"- What this step means: You are aiming to cut down half a serving of sugary drinks daily, like soda or sweetened tea.\n"
"- Why this helps your health: Reducing sugary drinks lowers extra sugar and calories, helping your blood sugar and weight.\n"
"- A realistic plan for you: I know sugary drinks can be a quick energy fix during shifts. Try swapping one sugary drink for water or unsweetened tea during your break. Keep a water bottle handy to sip throughout your shift. On days off, try flavored water with lemon or cucumber to keep it interesting.\n"
"- How this fits ADA guidelines: This matches ADA advice to reduce added sugars for better blood sugar and weight management.\n"
"\n"
"4. Working on wst (waist circumference): from 110.5 to 109.5 cm\n"
"- What this step means: You are working to reduce your waist size by 1 cm, from 110.5 to 109.5 cm.\n"
"- Why this helps your health: A smaller waist can mean less fat around your organs, which helps your blood sugar and heart health.\n"
"- A realistic plan for you: Losing waist size can be hard with your schedule and pain. Focus on small changes like choosing more vegetables and lean proteins at your late meals. Try to limit refined carbs like white bread or sweets. Pair this with your increased activity for better results.\n"
"- How this fits ADA guidelines: This fits ADA recommendations to support weight loss and reduce belly fat for better diabetes outcomes.\n"
"\n"
"5. Working on glu (blood sugar): from 182 to 177 mg/dL\n"
"- What this step means: You want to lower your blood sugar from 182 to 177 mg/dL, a small but important step down.\n"
"- Why this helps your health: Lower blood sugar helps your body work better and reduces risks of diabetes complications.\n"
"- A realistic plan for you: Managing blood sugar with your shift work and late meals is tricky. Try to eat balanced meals with protein and fiber at night to slow sugar spikes. Avoid sugary drinks as we discussed. Also, your added activity will help lower blood sugar naturally.\n"
"- How this fits ADA guidelines: This matches ADA advice to improve blood sugar through healthy eating and physical activity.\n"
"\n"
"6. Working on hb1ac (average blood sugar over time): from 8.6% to 8.5%\n"
"- What this step means: You are aiming to slightly lower your average blood sugar over time, from 8.6% to 8.5%.\n"
"- Why this helps your health: Even small improvements in this number can reduce risks of long-term diabetes complications.\n"
"- A realistic plan for you: This small change can come from the combined effects of better food choices, cutting sugary drinks, and moving more. Keep tracking your progress and celebrate small wins. If you can, write down what you eat and your activity to see patterns.\n"
"- How this fits ADA guidelines: This fits ADA guidance encouraging gradual improvements in blood sugar through lifestyle changes.\n"
"\n"
"7. Working on tyg (triglycerides): from 230 to 220 mg/dL\n"
"- What this step means: You want to lower your blood fats from 230 to 220 mg/dL.\n"
"- Why this helps your health: Lower triglycerides support your heart and blood vessels and reduce risks of heart disease.\n"
"- A realistic plan for you: To lower triglycerides, try to limit sugary and fried foods, especially at late meals. Choose healthier fats like nuts or olive oil if affordable. Continue your gentle activity, which also helps lower blood fats.\n"
"- How this fits ADA guidelines: This matches ADA advice to improve blood fats through diet and activity.\n"
"\n"
"8. Working on sys (systolic blood pressure): from 138 to 136 mmHg\n"
"- What this step means: You are aiming to lower your top blood pressure number slightly, from 138 to 136 mmHg.\n"
"- Why this helps your health: Lower blood pressure reduces strain on your heart and lowers risks of stroke and heart problems.\n"
"- A realistic plan for you: Managing blood pressure can be tough with stress and shift work. Try to reduce salt in your meals by cooking more at home when possible. Practice deep breathing or relaxation for a few minutes daily to help with stress. Keep up your increased activity as it also helps lower blood pressure.\n"
"- How this fits ADA guidelines: This fits ADA recommendations to support heart health through lifestyle changes.\n"
"\n"
"EVIDENCE USED (RAW ADA CHUNKS)\n"
"==============================\n"
"--- RL Action 1: mvpa ---\n"
"Management and reduction of weight is important for people with type 1 diabetes, type 2 diabetes, or prediabetes with overweight or obesity. To support weight loss and improve A1C, CVD risk factors, and well-being in adults with overweight or obesity and prediabetes or diabetes, MNT and DSMES services should include an individualized eating plan resulting in an energy deficit in combination with enhanced physical activity (50). Lifestyle intervention programs should be intensive and have frequent follow-up to achieve significant reductions in excess body weight and improve clinical indicators. Behavior modification goals should address physical activity, calorie restriction, healthy weight management strategies, and motivation.\n"
"#For all people with diabetes, baseline physical activity and time spent in sedentary behavior should be evaluated. People who do not meet activity guidelines should be encouraged to increase physical activity (e.g., walking, yoga, housework, gardening, swimming, and dancing) above baseline (278). Health care professionals should counsel people with diabetes to engage in aerobic and resistance exercise regularly (267). Aerobic activity bouts should last at least 10 min, with the goal of ∼30 min/day or more most days of the week for adults with type 2 diabetes. Daily exercise, or at least not allowing more than 2 days to elapse between exercise sessions, is recommended to decrease insulin resistance, regardless of diabetes type (279,280).\n"
"5.38 For all people with diabetes, evaluate baseline physical activity and time spent in sedentary behavior (i.e., quiet sitting, lying, and leaning). For people who do not meet activity guidelines, encourage an increase in physical activities (e.g., walking, yoga, housework, gardening, swimming, and dancing) above baseline. B Counsel that prolonged sitting should be interrupted at least every 30 min for blood glucose benefits. C\n"
"Many individuals with type 2 diabetes do not meet the recommended physical activity levels (150 min/week). Objective measurement by accelerometer in 871 individuals with type 2 diabetes showed that 44.2%, 42.6%, and 65.1% of White, African American, and Hispanic individuals, respectively, met the recommended physical activity threshold (256). An RCT in 1,366 individuals with prediabetes combined a physical activity intervention with text messaging and telephone support, which showed improvement in daily step count at 12 months compared with the control group, but this was not sustained at 48 months (257).\n"
"\n"
"--- RL Action 2: ac_week ---\n"
"Many individuals with type 2 diabetes do not meet the recommended physical activity levels (150 min/week). Objective measurement by accelerometer in 871 individuals with type 2 diabetes showed that 44.2%, 42.6%, and 65.1% of White, African American, and Hispanic individuals, respectively, met the recommended physical activity threshold (256). An RCT in 1,366 individuals with prediabetes combined a physical activity intervention with text messaging and telephone support, which showed improvement in daily step count at 12 months compared with the control group, but this was not sustained at 48 months (257).\n"
"A study in adults with type 1 diabetes found a dose-response inverse relationship between self-reported bouts of physical activity per week and A1C, BMI, hypertension, dyslipidemia, and diabetes-related complications such as hypoglycemia, DKA, retinopathy, and microalbuminuria (281), and higher physical activity reduces mortality risk in people with type 1 diabetes (260). Over time, activities should progress in intensity, frequency, and/or duration to at least 150 min/week of moderate-intensity exercise. Adults able to run at 6 mph (9.7 km/h) for at least 25 min can benefit sufficiently from shorter durations of vigorous-intensity activity or interval training (75 min/week) (267).\n"
"For all people with diabetes, baseline physical activity and time spent in sedentary behavior should be evaluated. People who do not meet activity guidelines should be encouraged to increase physical activity (e.g., walking, yoga, housework, gardening, swimming, and dancing) above baseline (278). Health care professionals should counsel people with diabetes to engage in aerobic and resistance exercise regularly (267). Aerobic activity bouts should last at least 10 min, with the goal of ∼30 min/day or more most days of the week for adults with type 2 diabetes. Daily exercise, or at least not allowing more than 2 days to elapse between exercise sessions, is recommended to decrease insulin resistance, regardless of diabetes type (279,280).\n"
"5.35 Counsel most adults with type 1 diabetes C and type 2 diabetes B to engage in 150 min or more of moderate- to vigorous-intensity aerobic activity per week, spread over at least 3 days/week, with no more than 2 consecutive days without activity. Shorter durations (minimum 75 min/week) of vigorous-intensity or interval training may be sufficient for more physically fit individuals.\n"
"\n"
"--- RL Action 3: sugary_drinks_per_day ---\n"
"Health care professionals should encourage reductions in foods and beverages with added sugars and promote reducing overall sugar intake and calories with or without the use of NNS. Assuring people with diabetes that NNS have undergone extensive safety evaluation by regulatory agencies and are continually monitored can allay unnecessary concern for harm. Health care professionals can regularly assess individual use of NNS based on the acceptable daily intake (amount of a substance considered safe to consume each day over a person’s life) and recommend moderation. See the chart from the FDA on safe levels of sweeteners found at fda.gov/food/food-additives-petitions/aspartame-and-other-sweeteners-food.\n"
"5.25 Advise people with diabetes and those at risk to replace sugar-sweetened beverages.\n"
"minimize consumption of red meat, sugar-sweetened beverages, sweets.\n"
"diabetes to improve glycemia, as this approach may be applied to a.\n"
"\n"
"--- RL Action 4: wst ---\n"
"Suggested citation: American Diabetes Association Professional Practice Committee. 8. Obesity and weight management for the prevention and treatment of type 2 diabetes: Standards of Care in Diabetes—2025. Diabetes Care 2025;48(Suppl. 1):S167—S180.\n"
"Most notably, the Surgical Treatment and Medications Potentially Eradicate Diabetes Efficiently (STAMPEDE) trial, which randomized 150 participants with type 2 diabetes, A1C >7.0%, and BMI 27–43 kg/m2 to receive either metabolic surgery or medical treatment for type 2 diabetes using glucose-lowering agents, found that 29% of those treated with RYGB and 23% of those treated with VSG achieved A1C of ≤6.0% after 5 years (47). Available data suggest an erosion of diabetes remission over time (48); 35–50% of individuals who initially achieve remission of diabetes eventually experience recurrence.\n"
"8.21 Consider metabolic surgery as a weight and glycemic management approach in people with diabetes with BMI ≥30.0 kg/m2 (or ≥27.5 kg/m2 in Asian American individuals) who are otherwise good surgical candidates. A\n"
"\n"
"--- RL Action 5: glu ---\n"
"diabetes to improve glycemia, as this approach may be applied to a.\n"
"Lifestyle interventions (i.e., changing nutrition and/or physical activity) also demonstrate benefits for depressive symptoms and A1C (295) on their own and when combined with CBT (453–455). Finally, a systematic review and meta-analysis found that use of GLP-1 RAs led to significant improvement in depressive symptoms among adults with type 2 diabetes (456). It is important to note that the medical treatment plan should also be monitored in response to reduction in depressive symptoms.\n"
"5.38 For all people with diabetes, evaluate baseline physical activity and time spent in sedentary behavior. For people who do not meet activity guidelines, encourage an increase in physical activities. Counsel that prolonged sitting should be interrupted at least every 30 min for blood glucose benefits.\n"
"disease risk A and improve glucose metabolism. B\n"
"\n"
"--- RL Action 6: hb1ac ---\n"
"diabetes to improve glycemia, as this approach may be applied to a.\n"
"5.38 For all people with diabetes, evaluate baseline physical activity and time spent in sedentary behavior. For people who do not meet activity guidelines, encourage an increase in physical activities. Counsel that prolonged sitting should be interrupted at least every 30 min for blood glucose benefits.\n"
"These nonpharmacologic interventions did not reduce A1C, triglycerides, or BMI (478). Qualitative research suggests that educational and behavioral interventions provide benefit via group support, accountability, and assistance with applying diabetes knowledge (479).\n"
"For all people with diabetes, baseline physical activity and time spent in sedentary behavior should be evaluated.\n"
"\n"
"--- RL Action 7: tyg ---\n"
"Suggested citation: American Diabetes Association Professional Practice Committee. 8. Obesity and weight management for the prevention and treatment of type 2 diabetes: Standards of Care in Diabetes—2025.\n"
"Most notably, the STAMPEDE trial...\n"
"Weight management pharmacotherapy has demonstrated multiple additional benefits beyond weight loss.\n"
"8.21 Consider metabolic surgery as a weight and glycemic management approach...\n"
"\n"
"--- RL Action 8: sys ---\n"
"diabetes to improve glycemia, as this approach may be applied to a.\n"
"5.38 For all people with diabetes, evaluate baseline physical activity and time spent in sedentary behavior.\n"
"Lifestyle interventions demonstrate benefits for depressive symptoms and A1C.\n"
"Management and reduction of weight is important for people with diabetes.\n"
"\n"
"\n"
"This is a demo lifestyle recommendation generated from a fixed example case. "
"In the full version of this tool, this section will provide personalized "
"guidance based on the patient's clinical and lifestyle data."
)


    # 🔹 일반 모드: 여기에서 실제 친구 모델을 호출하면 됨
    # 예시:
    # response_text = friend_model_api(features)
    # return response_text

    # 지금은 placeholder 텍스트만 넣어둠
    return (
        "This is a placeholder recommendation. "
        "Replace the body of get_recommendation() with a real call to your friend's model "
        "so that it can generate personalized lifestyle guidance based on the features dict."
    )


# --------------------
# 1. Session state 초기화
# --------------------
if "started" not in st.session_state:
    st.session_state.started = False
if "current_step" not in st.session_state:
    st.session_state.current_step = 0
if "confirm_missing" not in st.session_state:
    st.session_state.confirm_missing = False
if "pending_missing_step" not in st.session_state:
    st.session_state.pending_missing_step = None
if "pending_missing_labels" not in st.session_state:
    st.session_state.pending_missing_labels = []
if "context" not in st.session_state:
    st.session_state.context = ""
if "recommendation" not in st.session_state:
    st.session_state.recommendation = None
if "demo_mode" not in st.session_state:
    st.session_state.demo_mode = False

# --------------------
# 2. 스텝 정의 (마지막 2개: review, output)
# --------------------
STEPS = [
    ("demo", "🧍 Demographics"),
    ("anthro", "📏 Anthropometrics"),
    ("vital", "❤️ Vital Signs"),
    ("liver", "🧪 Liver Function"),
    ("renal", "🩸 Renal Function"),
    ("metabolic", "🫀 Metabolic & Lipid"),
    ("glycemic", "🩸 Glycemic Control"),
    ("inflam", "🔥 Inflammatory Markers"),
    ("cbc", "🧬 CBC"),
    ("lifestyle", "🏃 Lifestyle & Habits"),
    ("review", "🔍 Review & Context"),
    ("output", "📊 Lifestyle Recommendation"),
]

# 각 스텝별 필수 필드(key: session_state 키, value: 라벨)
REQUIRED_FIELDS = {
    "demo": {
        "gender_input": "Gender",
        "age_input": "Age (years)",
        "race_input": "Race/Hispanic Origin",
        "educ_input": "Education Level",
        "marital_input": "Marital Status",
        "house_input": "Household Size",
        "pov_input": "Poverty Index (PIR)",
    },
    "anthro": {
        "wt": "Weight (kg)",
        "ht": "Height (cm)",
        "bmi": "BMI (kg/m², editable)",
        "wst": "Waist Circumference (cm)",
        "hip": "Hip Circumference (cm)",
    },
    "vital": {
        "sys": "Systolic BP (mmHg)",
        "dia": "Diastolic BP (mmHg)",
        "pulse": "Pulse Rate (bpm)",
    },
    "liver": {
        "alt": "ALT (IU/L)",
        "ast": "AST (IU/L)",
        "ggt": "GGT (IU/L)",
        "albumin": "Albumin (g/dL)",
    },
    "renal": {
        "crea": "Creatinine (mg/dL)",
        "acratio": "Albumin/Creatinine Ratio (mg/g)",
    },
    "metabolic": {
        "chol": "Total Cholesterol (mg/dL)",
        "ldl": "LDL (mg/dL)",
        "hdl": "HDL (mg/dL)",
        "tyg": "TyG Index",
        "glu": "Fasting Glucose (mg/dL)",
        "insulin": "Insulin (µU/mL)",
    },
    "glycemic": {
        "h3a1c": "HbA1c (%)",
    },
    "inflam": {
        "crp": "hsCRP (mg/L)",
        "wbc": "White Blood Cells (10³/μL)",
    },
    "cbc": {
        "hb": "Hemoglobin (g/dL)",
        "hct": "Hematocrit (%)",
    },
    "lifestyle": {
        "mvpa": "MVPA (min/week)",
        "ac_week": "Alcohol Intake (drinks/week)",
        "veg_week": "Vegetarian Meals per Week",
        "sleep_avg": "Average Sleep Duration (h/night)",
        "bedtime_score": "Typical Bedtime",
    },
}

# 숫자형 필수 필드만 따로 정의
NUMERIC_REQUIRED_FIELDS = {
    "demo": ["age_input", "house_input", "pov_input"],
    "anthro": ["wt", "ht", "bmi", "wst", "hip"],
    "vital": ["sys", "dia", "pulse"],
    "liver": ["alt", "ast", "ggt", "albumin"],
    "renal": ["crea", "acratio"],
    "metabolic": ["chol", "ldl", "hdl", "tyg", "glu", "insulin"],
    "glycemic": ["h3a1c"],
    "inflam": ["crp", "wbc"],
    "cbc": ["hb", "hct"],
    "lifestyle": [
        "mvpa",
        "ac_week",
        "veg_week",
        "sleep_avg",
        # bedtime_score는 범주형 코드라 필수 numeric 체크에선 제외
    ],
}


def check_missing_numeric(step_id: str):
    """현재 스텝에서 비어 있는(0 또는 None) 숫자형 필수 필드만 체크"""
    missing = []
    numeric_keys = NUMERIC_REQUIRED_FIELDS.get(step_id, [])
    for key in numeric_keys:
        label = REQUIRED_FIELDS.get(step_id, {}).get(key, key)
        val = st.session_state.get(key, None)
        if val is None or (isinstance(val, (int, float)) and val == 0):
            missing.append(label)
    return missing


def build_features_from_session():
    """친구 모델에 넣을 features 딕셔너리 생성 (34개 + context + lifestyle 요약 변수)"""

    # 🔹 Demo 모드면 session_state 무시하고 항상 고정값 반환
    if st.session_state.get("demo_mode", False):
        return DEMO_FEATURES.copy()

    ss = st.session_state
    get = ss.get

    features = {
        # demo (모델용 숫자 인코딩)
        "gender": get("gender", 0),
        "race": get("race", 0),
        "marry": get("marry", 0),
        "age": get("age", 0),
        "educ": get("educ", 0),
        "house": get("house", 0),
        "pov": get("pov_input", 0.0),

        # anthropometrics
        "wt": get("wt", 0.0),
        "ht": get("ht", 0.0),
        "bmi": get("bmi", 0.0),
        "wst": get("wst", 0.0),
        "hip": get("hip", 0.0),

        # vital
        "sys": get("sys", 0.0),
        "dia": get("dia", 0.0),
        "pulse": get("pulse", 0.0),

        # liver
        "alt": get("alt", 0.0),
        "albumin": get("albumin", 0.0),
        "ast": get("ast", 0.0),
        "ggt": get("ggt", 0.0),

        # renal
        "crea": get("crea", 0.0),
        "acratio": get("acratio", 0.0),

        # metabolic
        "chol": get("chol", 0.0),
        "ldl": get("ldl", 0.0),
        "hdl": get("hdl", 0.0),
        "tyg": get("tyg", 0.0),
        "glu": get("glu", 0.0),
        "insulin": get("insulin", 0.0),

        # inflam
        "crp": get("crp", 0.0),
        "wbc": get("wbc", 0.0),

        # cbc
        "hb": get("hb", 0.0),
        "hct": get("hct", 0.0),

        # lifestyle
        "mvpa": get("mvpa", 0.0),
        "ac_week": get("ac_week", 0.0),
        "veg_week": get("veg_week", 0.0),
        "sleep_avg": get("sleep_avg", 0.0),
        "bedtime_score": get("bedtime_score", 0),

        # extra
        "h3a1c": get("h3a1c", 0.0),

        # context 텍스트
        "context": get("context", ""),
    }

    return features


def build_display_features_from_session():
    """
    리뷰용: 사용자가 실제로 화면에서 본/선택한 값 그대로 모아놓은 딕셔너리.
    Unknown / None / 0 은 전부 "None" 이라는 텍스트로 표시.
    """
    ss = st.session_state
    get = ss.get

    def norm_cat(val):
        """카테고리: Unknown / None / 빈문자 → 'None'"""
        if val is None:
            return "None"
        if isinstance(val, str) and val.strip().lower() == "unknown":
            return "None"
        if val == "":
            return "None"
        return val

    def norm_num(val):
        """숫자: None 또는 0 → 'None'"""
        if val is None:
            return "None"
        try:
            if float(val) == 0:
                return "None"
        except Exception:
            pass
        return val

    display_features = {
        # Demo (selected text 그대로)
        "Gender": norm_cat(get("gender_input", None)),
        "Age (years)": norm_num(get("age", get("age_input", None))),
        "Race/Hispanic Origin": norm_cat(get("race_input", None)),
        "Education Level": norm_cat(get("educ_input", None)),
        "Marital Status": norm_cat(get("marital_input", None)),
        "Household Size": norm_cat(get("house_input", None)),
        "Poverty Index (PIR)": norm_num(get("pov_input", None)),

        # Anthropometrics
        "Weight (kg)": norm_num(get("wt", None)),
        "Height (cm)": norm_num(get("ht", None)),
        "BMI (kg/m²)": norm_num(get("bmi", None)),
        "Waist Circumference (cm)": norm_num(get("wst", None)),
        "Hip Circumference (cm)": norm_num(get("hip", None)),

        # Vital Signs
        "Systolic BP (mmHg)": norm_num(get("sys", None)),
        "Diastolic BP (mmHg)": norm_num(get("dia", None)),
        "Pulse Rate (bpm)": norm_num(get("pulse", None)),

        # Liver
        "ALT (IU/L)": norm_num(get("alt", None)),
        "AST (IU/L)": norm_num(get("ast", None)),
        "GGT (IU/L)": norm_num(get("ggt", None)),
        "Albumin (g/dL)": norm_num(get("albumin", None)),

        # Renal
        "Creatinine (mg/dL)": norm_num(get("crea", None)),
        "Albumin/Creatinine Ratio (mg/g)": norm_num(get("acratio", None)),

        # Metabolic / Lipid
        "Total Cholesterol (mg/dL)": norm_num(get("chol", None)),
        "LDL (mg/dL)": norm_num(get("ldl", None)),
        "HDL (mg/dL)": norm_num(get("hdl", None)),
        "TyG Index": norm_num(get("tyg", None)),
        "Fasting Glucose (mg/dL)": norm_num(get("glu", None)),
        "Insulin (µU/mL)": norm_num(get("insulin", None)),

        # Glycemic
        "HbA1c (%)": norm_num(get("h3a1c", None)),

        # Inflammatory
        "hsCRP (mg/L)": norm_num(get("crp", None)),
        "White Blood Cells (10³/μL)": norm_num(get("wbc", None)),

        # CBC
        "Hemoglobin (g/dL)": norm_num(get("hb", None)),
        "Hematocrit (%)": norm_num(get("hct", None)),

        # Lifestyle
        "MVPA (min/week)": norm_num(get("mvpa", None)),
        "Alcohol Intake (drinks/week)": norm_num(get("ac_week", None)),
        "Vegetarian Meals per Week": norm_num(get("veg_week", None)),
        "Average Sleep Duration (h/night)": norm_num(get("sleep_avg", None)),
        "Typical Bedtime": norm_cat(get("bedtime_label", None)),

        # Context
        "Context": (
            get("context", "").strip()
            if get("context", "").strip() != ""
            else "None"
        ),
    }

    return display_features


def build_demo_display_features():
    """Demo 모드에서 리뷰 테이블에 보여줄 고정 케이스"""
    display_features = {
        "Gender": "Male",
        "Age (years)": 52,
        "Race/Hispanic Origin": "White",
        "Education Level": "Some college / AA degree",
        "Marital Status": "Married/Living with partner",
        "Household Size": 3,
        "Poverty Index (PIR)": 1.7,

        "Weight (kg)": 88.5,
        "Height (cm)": 173.0,
        "BMI (kg/m²)": 29.6,
        "Waist Circumference (cm)": 102.0,
        "Hip Circumference (cm)": 100.0,

        "Systolic BP (mmHg)": 138.0,
        "Diastolic BP (mmHg)": 86.0,
        "Pulse Rate (bpm)": 78.0,

        "ALT (IU/L)": 42.0,
        "AST (IU/L)": 36.0,
        "GGT (IU/L)": 65.0,
        "Albumin (g/dL)": 4.2,

        "Creatinine (mg/dL)": 1.0,
        "Albumin/Creatinine Ratio (mg/g)": 22.0,

        "Total Cholesterol (mg/dL)": 212.0,
        "LDL (mg/dL)": 138.0,
        "HDL (mg/dL)": 41.0,
        "TyG Index": 8.8,
        "Fasting Glucose (mg/dL)": 108.0,
        "Insulin (µU/mL)": 15.0,

        "HbA1c (%)": 5.9,

        "hsCRP (mg/L)": 3.8,
        "White Blood Cells (10³/μL)": 7.2,

        "Hemoglobin (g/dL)": 14.6,
        "Hematocrit (%)": 43.0,

        "MVPA (min/week)": 70.0,
        "Alcohol Intake (drinks/week)": 8.0,
        "Vegetarian Meals per Week": 5.0,
        "Average Sleep Duration (h/night)": 5.5,
        "Typical Bedtime": "11 pm–12 am",

        "Context": DEMO_FEATURES["context"],
    }
    return display_features


# --------------------
# 3. 인트로 화면
# --------------------
if not st.session_state.started:
    st.markdown(
        """
        <div style="text-align:center; margin-top:80px;">
            <h1>Diabetes Clinical Risk Assistant</h1>
            <h3>Turning routine clinical data into actionable lifestyle guidance.</h3>
            <p style="max-width:600px; margin: 20px auto; color:#555;">
                Our mission is to support clinicians with a simple, structured tool that collects key clinical,
                laboratory, and lifestyle data and turns it into practical, personalized habit-change recommendations.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    btn_col1, btn_col2, btn_col3 = st.columns([1, 2, 1])
    with btn_col2:
        if st.button("Let’s get started", use_container_width=True):
            st.session_state.started = True
            st.session_state.demo_mode = False
            st.session_state.current_step = 0

        # 🔹 Demo 버튼 추가
        if st.button("Demo (pre-filled case)", use_container_width=True):
            st.session_state.started = True
            st.session_state.demo_mode = True
            # 바로 review 스텝으로 보내기
            review_index = [i for i, (sid, _) in enumerate(STEPS) if sid == "review"][0]
            st.session_state.current_step = review_index
            st.rerun()

    st.stop()

# --------------------
# 4. 메인 레이아웃
# --------------------
left_col, right_col = st.columns([0.25, 0.75])

with left_col:
    st.markdown("### 📚 Sections")
    for i, (_, label) in enumerate(STEPS):
        if i == st.session_state.current_step:
            st.markdown(f"- **▶ {label}**")
        else:
            st.markdown(f"- {label}")

with right_col:
    step_id, step_label = STEPS[st.session_state.current_step]
    st.header(step_label)

    # --------------------
    # 각 스텝별 입력 폼
    # --------------------
    if step_id == "demo":
        # Gender + Unknown
        gender_input = st.selectbox(
            "Gender",
            ["Male", "Female", "Unknown"],
            index=None,
            placeholder="Select Gender",
            key="gender_input",
        )
        gender_mapping = {"Male": 1, "Female": 2, "Unknown": 0}
        gender = gender_mapping[gender_input] if gender_input else 0
        st.session_state["gender"] = gender

        age_input = numeric_input("Age (years)", min_value=0, key="age_input")
        if isinstance(age_input, (int, float)) and age_input != 0:
            age = int(age_input) if age_input < 80 else 80
        else:
            age = 0
        st.session_state["age"] = age

        # Race + Unknown
        race_input = st.selectbox(
            "Race/Hispanic Origin",
            [
                "Mexican American",
                "Other Hispanic",
                "White",
                "Black",
                "Asian",
                "Other",
                "Unknown",
            ],
            index=None,
            placeholder="Select Race",
            key="race_input",
        )
        race_mapping = {
            "Mexican American": 1,
            "Other Hispanic": 2,
            "White": 3,
            "Black": 4,
            "Asian": 5,
            "Other": 6,
            "Unknown": 0,
        }
        race = race_mapping[race_input] if race_input else 0
        st.session_state["race"] = race

        # Education + Unknown
        educ_input = st.selectbox(
            "Education Level",
            [
                "Less than 9th grade",
                "9-11th grade(Includes 12th grade with no diploma)",
                "High school graduate",
                "Some college / AA degree",
                "College draduate or above",
                "Refused",
                "Don't know",
                "Unknown",
            ],
            index=None,
            placeholder="Select Education Level",
            key="educ_input",
        )
        educ_mapping = {
            "Less than 9th grade": 1,
            "9-11th grade(Includes 12th grade with no diploma)": 2,
            "High school graduate": 3,
            "Some college / AA degree": 4,
            "College draduate or above": 5,
            "Refused": 6,
            "Don't know": 7,
            "Unknown": 0,
        }
        educ = educ_mapping[educ_input] if educ_input else 0
        st.session_state["educ"] = educ

        # Marital Status + Unknown
        marital_input = st.selectbox(
            "Marital Status",
            [
                "Married/Living with partner",
                "Widowed/Divorced/Seperated",
                "Never married",
                "Refused",
                "Don't know",
                "Unknown",
            ],
            index=None,
            placeholder="Select Marital Status",
            key="marital_input",
        )
        marital_mapping = {
            "Married/Living with partner": 1,
            "Widowed/Divorced/Seperated": 2,
            "Never married": 3,
            "Refused": 77,
            "Don't know": 99,
            "Unknown": 0,
        }
        marital = marital_mapping[marital_input] if marital_input else 0
        st.session_state["marry"] = marital  # 모델 컬럼명 marry

        # Household size + Unknown
        house_input = st.selectbox(
            "Household Size",
            list(range(1, 7)) + ["7 or more", "Unknown"],
            index=None,
            placeholder="Select Household Size",
            key="house_input",
        )
        if isinstance(house_input, int):
            house = house_input
        elif house_input == "7 or more":
            house = 7
        elif house_input == "Unknown":
            house = 0
        else:
            house = 0
        st.session_state["house"] = house

        pov_input = numeric_input(
            "Poverty Index (PIR)", min_value=0.0, step=0.01, key="pov_input"
        )

    elif step_id == "anthro":
        wt = numeric_input("Weight (kg)", min_value=0.0, key="wt")
        ht = numeric_input("Height (cm)", min_value=0.0, key="ht")
        bmi = numeric_input("BMI (kg/m², editable)", min_value=0.0, key="bmi")
        wst = numeric_input("Waist Circumference (cm)", min_value=0.0, key="wst")
        hip = numeric_input("Hip Circumference (cm)", min_value=0.0, key="hip")

    elif step_id == "vital":
        sys = numeric_input("Systolic BP (mmHg)", min_value=0, key="sys")
        dia = numeric_input("Diastolic BP (mmHg)", min_value=0, key="dia")
        pulse = numeric_input("Pulse Rate (bpm)", min_value=0, key="pulse")

    elif step_id == "liver":
        alt = numeric_input("ALT (IU/L)", min_value=0.0, key="alt")
        ast = numeric_input("AST (IU/L)", min_value=0.0, key="ast")
        ggt = numeric_input("GGT (IU/L)", min_value=0.0, key="ggt")
        albumin = numeric_input(
            "Albumin (g/dL)", min_value=0.0, step=0.1, key="albumin"
        )

    elif step_id == "renal":
        crea = numeric_input(
            "Creatinine (mg/dL)", min_value=0.0, step=0.1, key="crea"
        )
        acratio = numeric_input(
            "Albumin/Creatinine Ratio (mg/g)", min_value=0.0, key="acratio"
        )

    elif step_id == "metabolic":
        chol = numeric_input(
            "Total Cholesterol (mg/dL)", min_value=0.0, key="chol"
        )
        ldl = numeric_input("LDL (mg/dL)", min_value=0.0, key="ldl")
        hdl = numeric_input("HDL (mg/dL)", min_value=0.0, key="hdl")
        tyg = numeric_input("TyG Index", min_value=0.0, key="tyg")
        glu = numeric_input("Fasting Glucose (mg/dL)", min_value=0.0, key="glu")
        insulin = numeric_input(
            "Insulin (µU/mL)", min_value=0.0, key="insulin"
        )

    elif step_id == "glycemic":
        h3a1c = numeric_input(
            "HbA1c (%)", min_value=0.0, step=0.1, key="h3a1c"
        )

    elif step_id == "inflam":
        crp = numeric_input("hsCRP (mg/L)", min_value=0.0, key="crp")
        wbc = numeric_input(
            "White Blood Cells (10³/μL)", min_value=0.0, key="wbc"
        )

    elif step_id == "cbc":
        hb = numeric_input("Hemoglobin (g/dL)", min_value=0.0, key="hb")
        hct = numeric_input("Hematocrit (%)", min_value=0.0, key="hct")

    elif step_id == "lifestyle":
        # 기존 변수
        mvpa = numeric_input("MVPA (min/week)", min_value=0.0, key="mvpa")
        ac_week = numeric_input(
            "Alcohol Intake (drinks/week)", min_value=0.0, key="ac_week"
        )

        st.markdown("#### Weekly lifestyle pattern (summary)")

        # 1) 채식/플랜트 베이스드 식사 횟수 (주간 범위 선택)
        veg_label_options = [
            "0–3 meals/week",
            "4–6 meals/week",
            "7–10 meals/week",
            "11–14 meals/week",
            "15+ meals/week",
            "Unknown",
        ]
        # 내부용 숫자 값 (대략적인 대표값)
        veg_to_num = {
            "0–3 meals/week": 2.0,
            "4–6 meals/week": 5.0,
            "7–10 meals/week": 8.5,
            "11–14 meals/week": 12.5,
            "15+ meals/week": 17.0,
            "Unknown": 0.0,
        }

        veg_choice = st.selectbox(
            "Vegetarian / plant-based meals per week (approx.)",
            veg_label_options,
            index=None,
            placeholder="Select Vegetable Intake Amount",
            key="veg_week_label",
        )
        veg_week = veg_to_num.get(veg_choice, 0.0)
        st.session_state["veg_week"] = float(veg_week)

        # 2) 평균 수면 시간 (범위 선택)
        sleep_label_options = [
            "<3 h",
            "3–4 h",
            "4–5 h",
            "5–6 h",
            "6–7 h",
            ">7 h",
            "Unknown",
        ]
        sleep_to_num = {
            "<3 h": 2.5,
            "3–4 h": 3.5,
            "4–5 h": 4.5,
            "5–6 h": 5.5,
            "6–7 h": 6.5,
            ">7 h": 8.0,
            "Unknown": 0.0,
        }

        sleep_choice = st.selectbox(
            "Average sleep duration per night (last week)",
            sleep_label_options,
            index=None,
            placeholder="Select Sleeping Duration Time",
            key="sleep_avg_label",
        )
        sleep_avg = sleep_to_num.get(sleep_choice, 0.0)
        st.session_state["sleep_avg"] = float(sleep_avg)

        # 3) 취침 시간대 (bedtime, 시간대 범주)
        bedtime_label_options = [
            "Before 10 pm",
            "10–11 pm",
            "11 pm–12 am",
            "12–1 am",
            "After 1 am",
            "Unknown",
        ]
        # 내부용 숫자 점수(단계형 인코딩)
        bedtime_to_score = {
            "Before 10 pm": 1,
            "10–11 pm": 2,
            "11 pm–12 am": 3,
            "12–1 am": 4,
            "After 1 am": 5,
            "Unknown": 0,
        }

        bedtime_choice = st.selectbox(
            "Typical bedtime (last week)",
            bedtime_label_options,
            index=None,
            placeholder="Select bedtime",
            key="bedtime_label",
        )
        bedtime_score = bedtime_to_score.get(bedtime_choice, 0)
        st.session_state["bedtime_score"] = int(bedtime_score)

    elif step_id == "review":
        st.subheader("Review all variables")

        if st.session_state.get("demo_mode", False):
            display_features = build_demo_display_features()
        else:
            display_features = build_display_features_from_session()

        df_preview = pd.DataFrame([display_features])
        st.dataframe(df_preview)

        st.subheader("Patient contextual information (optional)")
        context_text = st.text_area(
            "Add any social / lifestyle / housing / work context here:",
            value=st.session_state.get("context", ""),
            height=200,
        )
        st.session_state["context"] = context_text

        st.info(
            "When you are ready, click the button below to generate a lifestyle recommendation "
            "based on these features."
        )
        if st.button("🚀 Generate lifestyle recommendation", use_container_width=True):
            features = build_features_from_session()
            rec_text = get_recommendation(features)
            st.session_state.recommendation = rec_text
            # output 페이지로 이동
            st.session_state.current_step += 1
            st.rerun()

    elif step_id == "output":
        #st.subheader("Lifestyle Recommendation")

        if st.session_state.recommendation is None:
            st.warning(
                "No recommendation yet. Please go back to the Review step and generate it."
            )
        else:
            st.markdown(st.session_state.recommendation)

        st.markdown("---")
        st.subheader("Context you provided")
        st.write(st.session_state.get("context", ""))

        if st.button("Start a new patient", use_container_width=True):
            # 간단 리셋
            for k in list(st.session_state.keys()):
                if k not in ["started"]:
                    del st.session_state[k]
            st.session_state.started = True
            st.session_state.current_step = 0
            st.rerun()

    # --------------------
    # 네비게이션 버튼 (review / output 제외)
    # --------------------
    if step_id not in ["review", "output"]:
        col_prev, col_next = st.columns([0.2, 0.8])

        # Back 버튼 제거 → 단방향 입력
        with col_next:
            lifestyle_index = [
                i for i, (sid, _) in enumerate(STEPS) if sid == "lifestyle"
            ][0]
            is_last_before_review = (
                st.session_state.current_step == lifestyle_index
            )

            btn_label = "Go to Review ➡" if is_last_before_review else "Next ➡"

            if st.button(btn_label, key=f"next_btn_{step_id}"):
                missing_num = check_missing_numeric(step_id)

                if missing_num and not st.session_state.confirm_missing:
                    st.session_state.confirm_missing = True
                    st.session_state.pending_missing_step = step_id
                    st.session_state.pending_missing_labels = missing_num
                    st.rerun()
                else:
                    st.session_state.confirm_missing = False
                    st.session_state.pending_missing_step = None
                    st.session_state.pending_missing_labels = []

                    st.session_state.current_step += 1
                    st.rerun()

        # 숫자 누락 시, Stay / Move on 선택 UI
        if (
            st.session_state.confirm_missing
            and st.session_state.pending_missing_step == step_id
        ):
            st.warning(
                "The following numeric fields are empty and will be treated as 0/None if you move on:\n\n"
                + ", ".join(st.session_state.pending_missing_labels)
            )

            c1, c2 = st.columns(2)
            with c1:
                if st.button("Stay on this page", key=f"stay_btn_{step_id}"):
                    st.session_state.confirm_missing = False
                    st.session_state.pending_missing_step = None
                    st.session_state.pending_missing_labels = []
                    st.rerun()

            with c2:
                if st.button("Move on anyway", key=f"move_on_btn_{step_id}"):
                    st.session_state.confirm_missing = False
                    st.session_state.pending_missing_step = None
                    st.session_state.pending_missing_labels = []
                    st.session_state.current_step += 1
                    st.rerun()

