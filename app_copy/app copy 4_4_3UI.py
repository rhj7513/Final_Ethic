
import streamlit as st
from PIL import Image
import time
import random

st.set_page_config(page_title="AI 돌봄 행동 추천 시스템", layout="wide")

st.title("🤖 노인 돌봄 AI 시스템")
st.markdown("노인의 **표정, 음성, 활동** 데이터를 기반으로 감정 및 건강 상태를 분석하고 적절한 돌봄 행동을 추천합니다.")

# Layout: 3 columns
left_col, center_col, right_col = st.columns([1.5, 1, 1.5])

# LEFT COLUMN - INPUT
with left_col:
    st.subheader("📥 데이터 입력")

    image_file = st.file_uploader("표정 이미지 업로드", type=["jpg", "jpeg", "png"], label_visibility="visible")
    audio_file = st.file_uploader("음성 파일 업로드 (선택)", type=["wav", "mp3"], label_visibility="visible")

    st.markdown("**🧍 활동 상태 선택**")
    activity_option = st.radio("현재 활동 상태를 선택하세요", ["정지", "앉아 있음", "걷는 중", "무기력함"])

    start_analysis = st.button("🔍 분석 시작!")

# CENTER COLUMN - LOADING / FLOW
with center_col:
    st.subheader("🔄 AI 분석 상태")
    if start_analysis and image_file:
        with st.spinner("AI가 데이터를 분석 중입니다..."):
            st.markdown("📡 **데이터 수신 중...**")
            time.sleep(1.5)
            st.markdown("🧠 **감정 상태 분석 중...**")
            time.sleep(1.5)
            st.markdown("💬 **돌봄 행동 추천 중...**")
            time.sleep(1.5)
            st.success("✅ 분석 완료!")
    elif not image_file and start_analysis:
        st.warning("⚠️ 먼저 표정 이미지를 업로드해주세요.")
    else:
        st.image("https://media.giphy.com/media/l0MYGb1LuZ3n7dRnO/giphy.gif", caption="AI 준비 중...", use_column_width=True)

# RIGHT COLUMN - OUTPUT
with right_col:
    st.subheader("📊 분석 결과")

    if start_analysis and image_file:
        emotion_result = random.choice(["외로움", "불안", "안정", "기쁨", "무기력"])
        health_flag = "양호" if activity_option in ["걷는 중", "앉아 있음"] else "주의 필요"

        st.write(f"**감정 상태:** :blue[{emotion_result}]")
        st.write(f"**건강 상태:** :orange[{health_flag}]")

        action_recommendations = {
            "외로움": "음악 재생 및 대화 시도",
            "불안": "보호자 호출 및 따뜻한 말 건네기",
            "안정": "가벼운 산책 유도 또는 휴식 유지",
            "기쁨": "함께 게임하거나 대화를 이어가기",
            "무기력": "가벼운 활동 권유 또는 휴식 권장"
        }

        recommended_action = action_recommendations.get(emotion_result, "상황 확인 필요")
        st.markdown(f"**추천 돌봄 행동:** 🟢 _{recommended_action}_")

        with st.expander("📈 리워드 반응 기록"):
            if st.button("😊 긍정적 반응 (Reward +1)"):
                st.success("🟢 리워드 +1 → 강화학습 반영 완료")
            if st.button("😟 부정적 반응 (No Reward)"):
                st.error("🔴 리워드 없음 → 학습 보류")

    else:
        st.info("왼쪽에서 데이터를 입력하고 '분석 시작!'을 눌러 결과를 확인하세요.")
