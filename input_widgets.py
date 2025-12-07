# input_widgets.py

import streamlit as st

import streamlit as st

def numeric_input(label, key, min_value=0.0, step=0.1):
    raw_key = key + "_raw"

    # 1) text_input에 value는 더이상 안 넘겨도 됨 (key로 state 관리)
    raw_value = st.text_input(
        label,
        key=raw_key,
        placeholder=f"{min_value}",
    )

    # 2) 아무 것도 안 쓴 경우 → None으로 간주
    if raw_value.strip() == "":
        st.session_state[key] = None
        return None

    # 3) 숫자 아닌 경우
    try:
        val = float(raw_value)
    except ValueError:
        st.error(f"{label}: 숫자를 입력해야 합니다.")
        st.session_state[key] = None
        return None

    # 4) 최소값보다 작은 경우
    if val < min_value:
        st.error(f"{label}: {min_value} 이상이어야 합니다.")
        st.session_state[key] = None
        return None

    # 5) 문제 없으면 검증된 값 저장
    st.session_state[key] = val
    return val


def bmi_input(label, key, auto_value):
    """BMI는 auto-calculated but editable 함수"""
    raw_key = key + "_raw"

    default_value = st.session_state.get(raw_key, str(auto_value) if auto_value else "")

    raw_value = st.text_input(
        label,
        value=default_value,
        placeholder="자동 계산 또는 직접 입력",
        key=raw_key,
    )

    try:
        val = float(raw_value)
    except:
        st.error("BMI: 숫자를 입력해야 합니다.")
        return None

    st.session_state[key] = val
    return val