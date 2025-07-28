
import streamlit as st
from PIL import Image
import time
import random
import base64

st.set_page_config(page_title="AI 돌봄 행동 추천 시스템", layout="wide")

st.markdown(
    "<h1 style='text-align: center; color: #4B8BBE;'>🤖 노인 돌봄 AI 시스템</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center; font-size:18px;'>표정, 음성, 활동 데이터를 기반으로 감정과 건강 상태를 분석하고<br>맞춤형 돌봄 행동을 추천하는 인공지능 시스템입니다.</p>",
    unsafe_allow_html=True
)

# 첫 번째 행: 입력과 분석 상태
col_input, col_status = st.columns([1.5, 2])

with col_input:
    st.markdown("### 📥 데이터 입력")

    image_file = st.file_uploader("**1. 표정 이미지 업로드**", type=["jpg", "jpeg", "png"])
    audio_file = st.file_uploader("**2. 음성 파일 업로드 (선택)**", type=["wav", "mp3"])
    activity_option = st.radio("**3. 활동 상태 선택**", ["정지", "앉아 있음", "걷는 중", "무기력함"], horizontal=True)
    start_analysis = st.button("🔍 분석 시작!", use_container_width=True)

with col_status:
    st.markdown("### 🔄 AI 분석 상태")
    st.markdown("---")
    if start_analysis and image_file:
        with st.spinner("AI가 데이터를 분석 중입니다..."):
            st.markdown("📡 <b>데이터 수신 중...</b>", unsafe_allow_html=True)
            time.sleep(1.0)
            st.markdown("🧠 <b>감정 상태 분석 중...</b>", unsafe_allow_html=True)
            time.sleep(1.0)
            st.markdown("💬 <b>돌봄 행동 추천 중...</b>", unsafe_allow_html=True)
            time.sleep(1.0)
            st.success("✅ 분석 완료!")
    elif not image_file and start_analysis:
        st.warning("⚠️ 먼저 표정 이미지를 업로드해주세요.")
    else:
        st.image("https://media.giphy.com/media/l0MYGb1LuZ3n7dRnO/giphy.gif", caption="AI 준비 중...", use_column_width=True)

# 두 번째 행: 분석 결과
if start_analysis and image_file:
    st.markdown("---")
    st.markdown("## 📊 분석 결과", unsafe_allow_html=True)

    emotion_result = random.choice(["외로움", "불안", "안정", "기쁨", "무기력"])
    health_flag = "양호" if activity_option in ["걷는 중", "앉아 있음"] else "주의 필요"

    image_map = {
        "외로움": "https://i.ibb.co/2vbQ2jk/sad.png",
        "불안": "https://i.ibb.co/0jLPMTG/anxious.png",
        "안정": "https://i.ibb.co/S6KkVbw/stable.png",
        "기쁨": "https://i.ibb.co/Zz5FhJL/happy.png",
        "무기력": "https://i.ibb.co/Dp8YXqG/tired.png"
    }

    st.markdown("### 🧠 감정 상태")
    st.image(image_map.get(emotion_result, ""), width=160, caption=emotion_result)
    st.markdown(f"<h3 style='color:steelblue'>{emotion_result}</h3>", unsafe_allow_html=True)
    with st.expander("🔎 왜 이런 감정 상태가 나왔나요?"):
        st.write(f"AI는 표정 이미지에서 **{emotion_result}**에 해당하는 특징(눈썹 위치, 입꼬리 방향 등)을 감지했기 때문입니다.")

    st.markdown("### 🏥 건강 상태")
    st.markdown(f"<h3 style='color:darkorange'>{health_flag}</h3>", unsafe_allow_html=True)
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
    tts_text = {
        "외로움": "할머니~ 오늘은 뭐하고 지내셨어요? 함께 이야기 나눠볼까요?",
        "불안": "할아버지, 괜찮으세요? 보호자분을 불러드릴게요.",
        "안정": "오늘은 컨디션이 괜찮으신 것 같아요. 산책이나 휴식은 어떠세요?",
        "기쁨": "기분이 좋아보이시네요! 즐거운 대화를 이어가볼까요?",
        "무기력": "많이 지치셨나요? 잠깐 쉬시거나 간단한 활동을 해볼까요?"
    }

    recommended_action = action_recommendations.get(emotion_result, "상황 확인 필요")
    st.markdown("### 🤖 추천 돌봄 행동")
    st.markdown(f"<h3 style='color:green'>{recommended_action}</h3>", unsafe_allow_html=True)
    with st.expander("🔎 이 행동은 왜 추천된 건가요?"):
        st.write(f"현재 감정 상태가 **{emotion_result}**로 분류되어, 이에 적합한 돌봄 행동으로 **{recommended_action}**이 추천되었습니다.")

    st.markdown("### 🔊 음성 출력 (시뮬레이션)")
    st.audio(f"https://tts-api.com/tts.mp3?q={tts_text.get(emotion_result)}")

else:
    st.info("왼쪽에서 데이터를 입력하고 '분석 시작!'을 눌러 결과를 확인하세요.")
