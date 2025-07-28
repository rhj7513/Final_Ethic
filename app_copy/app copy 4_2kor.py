import streamlit as st
import pandas as pd
import random
from PIL import Image
import io
import base64

# 페이지 설정
st.set_page_config(page_title="노인 돌봄 AI 웹앱", page_icon="🤖", layout="wide")

# 앱 제목
st.title("노인 돌봄 AI: 감정 분석 및 돌봄 추천")
st.write("이 앱은 노인의 표정, 음성, 활동 데이터를 분석하여 감정 상태를 파악하고 적절한 돌봄 행동을 추천합니다.")

# 튜토리얼 섹션
st.header("📚 튜토리얼: 이 앱을 사용하는 방법")
st.markdown("""
안녕하세요, 중학생 여러분! 이 앱은 노인의 감정을 이해하고 어떻게 도와줄지 제안하는 인공지능 앱이에요. 아래 단계를 따라 사용해보세요:

1. **데이터 입력**: 노인의 표정 이미지, 음성 톤, 활동 데이터를 입력합니다. (지금은 시뮬레이션 데이터를 사용해요!)
2. **감정 분석**: 앱이 데이터를 분석해서 노인이 어떤 감정을 느끼는지 알려줍니다. (예: 외로움, 불안, 기쁨)
3. **돌봄 추천**: 분석 결과를 바탕으로 어떤 행동을 하면 좋을지 추천해줍니다. (예: 대화하기, 음악 틀어주기)
4. **반응 기록**: 추천 행동 후 노인의 반응을 기록해서 더 나은 추천을 할 수 있게 학습합니다.

**시뮬레이션 모드**에서는 가짜 데이터를 사용해서 연습해볼 거예요. 아래에서 시작해봅시다!
""")

# 시뮬레이션 데이터 생성
def generate_sample_data():
    emotions = ["외로움", "불안", "기쁨", "안정"]
    activities = ["앉아있음", "걷기", "장시간 정지"]
    voice_tones = ["떨리는 목소리", "차분한 목소리", "활기찬 목소리"]
    return {
        "emotion": random.choice(emotions),
        "activity": random.choice(activities),
        "voice_tone": random.choice(voice_tones)
    }

# 돌봄 행동 추천
def recommend_action(emotion, activity, voice_tone):
    actions = {
        "외로움": ["대화 시도", "음악 재생"],
        "불안": ["보호자 호출", "휴식 권유"],
        "기쁨": ["대화 시도", "활동 장려"],
        "안정": ["휴식 권유", "음악 재생"]
    }
    return random.choice(actions.get(emotion, ["대화 시도"]))

# 반응 기록 및 리워드 계산
def record_response(action, response):
    reward = 1 if response == "긍정적" else -1
    return reward

# 이미지 업로드 및 표시
def display_image(image_file):
    if image_file is not None:
        image = Image.open(image_file)
        st.image(image, caption="업로드된 표정 이미지", width=300)
        return image
    return None

# 메인 앱
st.header("🎯 돌봄 AI 사용해보기")

# 시뮬레이션 데이터 사용 여부
use_simulation = st.checkbox("시뮬레이션 데이터로 테스트하기", value=True)

if use_simulation:
    st.subheader("시뮬레이션 데이터")
    if st.button("데이터 생성"):
        sample_data = generate_sample_data()
        st.session_state["sample_data"] = sample_data
        st.write(f"**감정 상태**: {sample_data['emotion']}")
        st.write(f"**활동**: {sample_data['activity']}")
        st.write(f"**음성 톤**: {sample_data['voice_tone']}")
else:
    st.subheader("직접 데이터 입력")
    uploaded_image = st.file_uploader("노인의 표정 이미지 업로드", type=["jpg", "png"])
    activity = st.selectbox("활동 선택", ["앉아있음", "걷기", "장시간 정지"])
    voice_tone = st.selectbox("음성 톤 선택", ["떨리는 목소리", "차분한 목소리", "활기찬 목소리"])
    display_image(uploaded_image)

# 감정 분석 및 추천
if st.button("감정 분석 및 돌봄 행동 추천"):
    if use_simulation and "sample_data" in st.session_state:
        data = st.session_state["sample_data"]
        emotion = data["emotion"]
        activity = data["activity"]
        voice_tone = data["voice_tone"]
    else:
        emotion = "외로움"  # 기본값 (실제로는 이미지/음성 분석 필요)
        activity = activity if not use_simulation else "앉아있음"
        voice_tone = voice_tone if not use_simulation else "차분한 목소리"

    st.subheader("분석 결과")
    st.write(f"**현재 감정 상태**: {emotion}")
    st.write(f"**활동 패턴**: {activity}")
    st.write(f"**음성 톤**: {voice_tone}")

    action = recommend_action(emotion, activity, voice_tone)
    st.session_state["recommended_action"] = action
    st.write(f"**추천 돌봄 행동**: {action}")

# 반응 기록
if "recommended_action" in st.session_state:
    st.subheader("노인의 반응 기록")
    response = st.radio("노인의 반응", ["긍정적", "부정적"])
    if st.button("반응 저장"):
        reward = record_response(st.session_state["recommended_action"], response)
        st.write(f"**리워드 점수**: {reward}")
        st.success("반응이 저장되었습니다! AI가 더 나은 추천을 위해 학습합니다.")

# 데이터셋 정보
st.header("ℹ️ 데이터셋 정보")
st.markdown("""
이 앱은 다음과 같은 데이터셋을 활용할 수 있습니다:
- **Kaggle 표정 이미지 데이터셋**: 노인의 감정(외로움, 불안 등)을 분석하기 위한 얼굴 이미지
- **Kaggle 음성 감정 데이터셋**: 음성 톤을 통해 감정을 파악
- **ResearchGate 노인 반응 데이터**: 돌봄 행동에 대한 노인의 반응 데이터

중학생 여러분이 직접 역할극을 통해 데이터를 만들 수도 있어요! 예를 들어, '불안한 노인' 역할을 연기하고 그 표정과 음성을 녹화해서 앱에 넣어볼 수 있습니다.
""")

# 기술 윤리 설명
st.header("🤔 기술 윤리: AI와 돌봄")
st.markdown("""
AI가 노인을 돌보는 데 사용될 때, 우리는 **윤리적 책임**을 생각해야 해요. 예를 들어:
- AI가 노인의 감정을 잘못 이해하면 어떤 일이 생길까요?
- 자동화된 돌봄이 사람의 따뜻한 손길을 완전히 대체할 수 있을까요?
- AI가 보호자를 부르는 대신 음악을 틀라고 잘못 추천하면 어떻게 될까요?

이런 질문들을 생각하며, 기술이 사람을 더 행복하게 만드는 방법을 고민해보세요!
""")