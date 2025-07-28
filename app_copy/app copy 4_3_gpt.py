
import streamlit as st
from PIL import Image
import numpy as np
import random

st.set_page_config(page_title="AI Elder Care Recommender", layout="wide")

st.title("🧓 AI 돌봄 행동 추천 시스템")
st.markdown("노인의 표정, 음성 톤, 움직임 데이터를 기반으로 감정 및 건강 상태를 분석하고, 상황에 맞는 돌봄 행동을 추천하는 AI 시스템입니다.")

with st.expander("🧭 튜토리얼 보기"):
    st.markdown("""
    **사용 방법**  
    1. 노인의 표정 이미지, 음성 톤(선택), 활동 데이터를 입력하세요.  
    2. AI가 감정 상태(예: 외로움, 불안, 안정 등)를 분석합니다.  
    3. 분석 결과에 따라 추천 돌봄 행동(예: 대화 시도, 보호자 호출 등)을 제공합니다.  
    4. 시뮬레이션을 통해 AI의 행동 추천에 대한 반응을 강화학습에 활용할 수 있습니다.
    """)

st.header("📥 입력 데이터 업로드")

image_file = st.file_uploader("1. 노인의 표정 이미지 업로드", type=["png", "jpg", "jpeg"])
activity_option = st.selectbox("2. 활동(움직임) 상태 선택", ["정지", "앉아 있음", "걷는 중", "무기력함"])

st.subheader("🧠 AI 감정 및 건강 상태 분석")

if image_file:
    image = Image.open(image_file)
    st.image(image, caption="입력된 노인 표정 이미지", use_column_width=True)

    # 샘플 분류 결과 시뮬레이션
    emotion_result = random.choice(["외로움", "불안", "안정", "기쁨", "무기력"])
    health_flag = "양호" if activity_option in ["걷는 중", "앉아 있음"] else "주의 필요"

    st.success(f"✔️ 감정 상태 분석 결과: **{emotion_result}**")
    st.warning(f"⚠️ 건강 상태 평가: **{health_flag}**")

    st.subheader("🤖 추천 돌봄 행동")
    action_recommendations = {
        "외로움": "음악 재생 및 대화 시도",
        "불안": "보호자 호출 및 따뜻한 말 건네기",
        "안정": "가벼운 산책 유도 또는 휴식 유지",
        "기쁨": "함께 게임하거나 대화를 이어가기",
        "무기력": "가벼운 활동 권유 또는 휴식 권장"
    }

    recommended_action = action_recommendations.get(emotion_result, "상황 확인 필요")
    st.info(f"🌱 추천 행동: **{recommended_action}**")

    st.subheader("📊 반응 기록 시뮬레이션")
    if st.button("긍정적 반응이면 클릭 (+Reward)"):
        st.success("🟢 리워드 +1 → 강화학습 반영 완료")
    if st.button("부정적 반응이면 클릭 (No Reward)"):
        st.error("🔴 리워드 없음 → 학습 보류")

else:
    st.info("표정 이미지를 업로드하면 분석이 시작됩니다.")
