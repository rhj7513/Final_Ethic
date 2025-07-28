import streamlit as st
from PIL import Image
import time, random, requests, os

# 네이버 TTS를 위한 설정 (환경 변수 또는 직접 삽입)
CLIENT_ID = os.getenv("NAVER_TTS_CLIENT_ID", "YOUR_CLIENT_ID")
CLIENT_SECRET = os.getenv("NAVER_TTS_CLIENT_SECRET", "YOUR_CLIENT_SECRET")

def get_tts_mp3(text):
    url = "https://naveropenapi.apigw.ntruss.com/tts-premium/v1/tts"
    headers = {
        "X-NCP-APIGW-API-KEY-ID": CLIENT_ID,
        "X-NCP-APIGW-API-KEY": CLIENT_SECRET
    }
    data = {
        "speaker": "mijin",
        "volume": 0,
        "speed": 0,
        "pitch": 0,
        "format": "mp3",
        "text": text
    }
    res = requests.post(url, headers=headers, data=data)
    return res.content if res.status_code == 200 else None

st.set_page_config(page_title="AI 돌봄 행동 추천 시스템", layout="wide")
st.markdown("<h1 style='text-align: center; color: #4B8BBE;'>🤖 노인 돌봄 AI 시스템</h1>", unsafe_allow_html=True)

# 첫 행: 입력 + 분석 상태
col_in, col_status = st.columns([1.5, 2])

with col_in:
    st.subheader("📥 데이터 입력")
    image_file = st.file_uploader("표정 이미지 업로드", type=["jpg","jpeg","png"])
    audio_file = st.file_uploader("음성 파일 업로드 (선택)", type=["wav","mp3"])
    activity = st.radio("활동 상태", ["정지","앉아 있음","걷는 중","무기력함"], horizontal=True)
    start = st.button("🔍 분석 시작!")

with col_status:
    st.subheader("🔄 AI 분석 상태")
    st.markdown("---")
    if start:
        if image_file:
            with st.spinner("AI 분석 중..."):
                st.markdown("📡 데이터 수신 중...")
                time.sleep(1)
                st.markdown("🧠 감정 및 건강 분석 중...")
                time.sleep(1)
                st.markdown("💬 추천 행동 생성 중...")
                time.sleep(1)
                st.success("✅ 분석 완료!")
        else:
            st.warning("⚠️ 이미지가 필요합니다!")

# 두 번째 행: 분석 결과 (분석 후에만 출력)
if start and image_file:
    st.markdown("---")
    st.subheader("📊 분석 결과")

    # 샘플 결과
    emotion = random.choice(["외로움","불안","안정","기쁨","무기력"])
    health = "양호" if activity in ["걷는 중","앉아 있음"] else "주의 필요"
    action_map = {
        "외로움":"음악 재생 및 대화 시도",
        "불안":"보호자 호출 및 따뜻한 말 건네기",
        "안정":"가벼운 산책 유도 또는 휴식 유지",
        "기쁨":"게임하거나 대화",
        "무기력":"가벼운 활동 권유 또는 휴식 권장"
    }
    action = action_map.get(emotion, "상황 확인 필요")
    explain_map = {
        emotion: f"표정에서 {emotion} 특징이 감지되었습니다.",
        health: "활동 상태 기반 건강 평가 결과입니다.",
        action: f"{emotion} 상태이므로 '{action}'을 추천했습니다."
    }
    # 이미지 맵 (URL은 예시입니다)
    imgs = {
        "외로움":"https://i.ibb.co/2vbQ2jk/sad.png",
        "불안":"https://i.ibb.co/0jLPMTG/anxious.png",
        "안정":"https://i.ibb.co/S6KkVbw/stable.png",
        "기쁨":"https://i.ibb.co/Zz5FhJL/happy.png",
        "무기력":"https://i.ibb.co/Dp8YXqG/tired.png"
    }

    st.image(imgs.get(emotion), width=180)
    st.markdown(f"### 🧠 감정 상태: **{emotion}**")
    with st.expander("🔎 설명"):
        st.write(explain_map[emotion])

    st.markdown(f"### 🏥 건강 상태: **{health}**")
    with st.expander("🔎 설명"):
        st.write(explain_map[health])

    st.markdown(f"### 🤖 추천 행동: **{action}**")
    with st.expander("🔎 설명"):
        st.write(explain_map[action])

    # TTS 출력
    tts_text = {
        "외로움":"할머니, 외로움이 느껴지시는군요. 음악을 틀어드릴까요?",
        "불안":"할아버지, 혹시 불안하신가요? 보호자를 호출해드릴까요?",
        "안정":"오늘 상태가 안정적으로 보여요. 잠시 산책은 어떠세요?",
        "기쁨":"기분이 좋아 보이세요! 함께 대화를 나눠볼까요?",
        "무기력":"무기력해 보이세요. 잠깐 쉬거나 움직임을 도와드릴까요?"
    }
    audio_data = get_tts_mp3(tts_text[emotion])
    if audio_data:
        st.audio(audio_data, format="audio/mp3")
    else:
        st.error("음성 생성에 실패했습니다.")
