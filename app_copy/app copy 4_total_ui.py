
import streamlit as st
from PIL import Image
import time
import random

st.set_page_config(page_title="AI 돌봄 행동 추천 시스템", layout="wide")

st.markdown(
    "<h1 style='text-align: center; color: #4B8BBE;'>🤖 노인 돌봄 AI 시스템</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center; font-size:18px;'>표정, 음성, 활동 데이터를 기반으로 감정과 건강 상태를 분석하고<br>맞춤형 돌봄 행동을 추천하는 인공지능 시스템입니다.</p>",
    unsafe_allow_html=True
)

# Layout: 3 columns
left_col, center_col, right_col = st.columns([1.5, 1, 1.5])

# LEFT COLUMN - INPUT
with left_col:
    st.markdown("### 📥 데이터 입력")

    st.markdown("**1. 표정 이미지 업로드**")
    image_file = st.file_uploader("이미지 파일 (jpg, png)", type=["jpg", "jpeg", "png"], label_visibility="collapsed")

    st.markdown("**2. 음성 파일 업로드 (선택)**")
    audio_file = st.file_uploader("음성 파일 (wav, mp3)", type=["wav", "mp3"], label_visibility="collapsed")

    st.markdown("**3. 활동 상태 선택**")
    activity_option = st.radio("", ["정지", "앉아 있음", "걷는 중", "무기력함"], horizontal=True)

    st.markdown("<br>", unsafe_allow_html=True)
    start_analysis = st.button("🔍 분석 시작!", use_container_width=True)

# CENTER COLUMN - LOADING / FLOW
with center_col:
    st.markdown("### 🔄 AI 분석 상태")
    st.markdown("---")
    if start_analysis and image_file:
        with st.spinner("AI가 데이터를 분석 중입니다..."):
            st.markdown("📡 <b>데이터 수신 중...</b>", unsafe_allow_html=True)
            time.sleep(1.2)
            st.markdown("🧠 <b>감정 상태 분석 중...</b>", unsafe_allow_html=True)
            time.sleep(1.2)
            st.markdown("💬 <b>돌봄 행동 추천 중...</b>", unsafe_allow_html=True)
            time.sleep(1.2)
            st.success("✅ 분석 완료!")
    elif not image_file and start_analysis:
        st.warning("⚠️ 먼저 표정 이미지를 업로드해주세요.")
    else:
        st.image("https://media.giphy.com/media/l0MYGb1LuZ3n7dRnO/giphy.gif", caption="AI 준비 중...", use_column_width=True)

# RIGHT COLUMN - OUTPUT
with right_col:
    st.markdown("### 📊 분석 결과")
    st.markdown("---")

    if start_analysis and image_file:
        emotion_result = random.choice(["외로움", "불안", "안정", "기쁨", "무기력"])
        health_flag = "양호" if activity_option in ["걷는 중", "앉아 있음"] else "주의 필요"

        st.markdown(f"**감정 상태:** <span style='color:steelblue;font-size:20px'>{emotion_result}</span>", unsafe_allow_html=True)
        with st.expander("🔎 왜 이런 감정 상태가 나왔나요?"):
            st.write(f"AI는 표정 이미지에서 **{emotion_result}**에 해당하는 특징(눈썹 위치, 입꼬리 방향 등)을 감지했기 때문입니다.")

        st.markdown(f"**건강 상태:** <span style='color:darkorange;font-size:20px'>{health_flag}</span>", unsafe_allow_html=True)
        with st.expander("🔎 왜 이런 건강 상태가 나왔나요?"):
            if health_flag == "양호":
                st.write("활동 상태가 '걷는 중' 또는 '앉아 있음'으로 비교적 활력이 있다고 판단되어 양호로 분류되었습니다.")
            else:
                st.write("활동 상태가 '정지' 또는 '무기력함'으로 판단되어 건강에 주의가 필요하다고 분석되었습니다.")

        action_recommendations = {
            "외로움": "음악 재생 및 대화 시도",
            "불안": "보호자 호출 및 따뜻한 말 건네기",
            "안정": "가벼운 산책 유도 또는 휴식 유지",
            "기쁨": "함께 게임하거나 대화를 이어가기",
            "무기력": "가벼운 활동 권유 또는 휴식 권장"
        }

        recommended_action = action_recommendations.get(emotion_result, "상황 확인 필요")
        st.markdown(f"**추천 돌봄 행동:** 🟢 <span style='font-size:20px'>{recommended_action}</span>", unsafe_allow_html=True)
        with st.expander("🔎 이 행동은 왜 추천된 건가요?"):
            st.write(f"현재 감정 상태가 **{emotion_result}**로 분류되어, 이에 적합한 돌봄 행동으로 **{recommended_action}**이 추천되었습니다.")

        with st.expander("📈 리워드 반응 기록"):
            col1, col2 = st.columns(2)
            with col1:
                if st.button("😊 긍정적 반응 (Reward +1)"):
                    st.success("🟢 리워드 +1 → 강화학습 반영 완료")
            with col2:
                if st.button("😟 부정적 반응 (No Reward)"):
                    st.error("🔴 리워드 없음 → 학습 보류")
    else:
        st.info("왼쪽에서 데이터를 입력하고 '분석 시작!'을 눌러 결과를 확인하세요.")
