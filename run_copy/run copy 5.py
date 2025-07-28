import streamlit as st

# 영상 데이터
video_urls = [
    'https://www.youtube.com/watch?v=h9nQNPXPWig',
    'https://www.youtube.com/watch?v=eir-zqegNV8',
    'https://www.youtube.com/watch?v=iZhI5oD8zwM',
    'https://www.youtube.com/watch?v=oiz6hyvTbXY',
]
video_titles = [
    "돌봄 로봇 개요",
    "Paro (치유 인형)",
    "Pepper (감정인식 로봇)",
    "효돌이 (한국형 AI 돌봄로봇)"
]

# 페이지 설정
st.set_page_config(layout="wide", page_title="EthicApp")
st.title("Ethic is good for us")

# 세션 상태 초기화
if 'video_index' not in st.session_state:
    st.session_state.video_index = 0
# if 'section' not in st.session_state:
#     st.session_state.section = None
if 'section' not in st.session_state:
    st.session_state.section = "video"  # 기본값은 영상 탭

# 사이드바 메뉴
st.sidebar.subheader("Menu...")
if st.sidebar.button("📺 AI 돌봄 로봇이란?"):
    st.session_state.section = "video"
if st.sidebar.button("🧠 윤리적 문제는?"):
    st.session_state.section = "ethics"
if st.sidebar.button("✍️ 나의 생각은?"):
    st.session_state.section = "opinion"

# 학생 데이터 보기 버튼
show_data = st.sidebar.button("📂 학생데이터 가져오기")

# 📐 화면 분할 (왼쪽 content, 오른쪽 tips)
col1, col2 = st.columns((4, 1))

# 왼쪽 콘텐츠 영역
with col1:
    if st.session_state.section == "video":
        current_index = st.session_state.video_index
        st.subheader(f"👀 영상으로 보는 'AI 돌봄 로봇' – {video_titles[current_index]}")
        st.video(video_urls[current_index])

        prev_col, next_col = st.columns([1, 1])
        with prev_col:
            if st.button("⬅️ 이전 영상", use_container_width=True, key="prev"):
                st.session_state.video_index = (current_index - 1) % len(video_urls)
                st.experimental_rerun()
        with next_col:
            if st.button("다음 영상 ➡️", use_container_width=True, key="next"):
                st.session_state.video_index = (current_index + 1) % len(video_urls)
                st.experimental_rerun()

        st.caption(f"📼 현재 영상: {current_index + 1} / {len(video_urls)}")

    elif st.session_state.section == "ethics":
        st.subheader("🤖 돌봄 로봇의 윤리")
        st.markdown("""
        - Pepper, Paro, 효돌이와 같은 AI 로봇이 인간을 어떻게 돌보는지 살펴보세요.  
        - 돌봄은 따뜻함인가, 효율성인가?  
        - 감정 인식, 인간 대체, 책임성 등의 윤리적 쟁점을 함께 고민해보세요.
        """)

    elif st.session_state.section == "opinion":
        st.subheader("✍️ 나의 생각을 적어보세요")

        st.markdown("<p style='font-size:20px; font-weight:bold; margin-bottom:5px;'>이름을 입력하세요</p>", unsafe_allow_html=True)
        user_name = st.text_input(label="", key="name", label_visibility="collapsed")

        st.markdown("<p style='font-size:20px; font-weight:bold; margin-bottom:5px;'>돌봄 로봇이 왜 필요할까? 영상을 시청 후 자유롭게 작성해주세요.</p>", unsafe_allow_html=True)
        user_opinion = st.text_area(label="", key="opinion", label_visibility="collapsed")

        submit = st.button("제출하기", key="submit")
        if submit:
            if user_name.strip() == "" or user_opinion.strip() == "":
                st.warning("이름과 의견을 모두 입력해주세요.")
            else:
                with open("./data/data.txt", "a", encoding="utf-8") as f:
                    f.write(f"[이름] {user_name}\n[의견] {user_opinion}\n{'-'*40}\n")
                st.success("의견이 성공적으로 제출되었습니다. 감사합니다!")

    # 학생 의견 보기
    if show_data:
        st.markdown("### 📋 제출된 학생 의견")
        try:
            with open("./data/data.txt", "r", encoding="utf-8") as f:
                data = f.read()
                if data.strip() == "":
                    st.info("아직 제출된 의견이 없습니다.")
                else:
                    st.text(data)
        except FileNotFoundError:
            st.error("data.txt 파일이 존재하지 않습니다.")

# 오른쪽 tips 영역
with col2:
    st.subheader("💡 Tips...")
    st.info("""
    ▸ 돌봄 로봇은 인간을 대신할 수 있을까요?  
    ▸ 감정을 인식하고 반응하는 AI는 인간과 같을까요?  
    ▸ 우리는 이 기술을 어떻게 바라보아야 할까요?
    """)
    st.markdown("---")
    st.write("👉 아래 영상은 수업 도입용으로 사용 가능합니다.")
