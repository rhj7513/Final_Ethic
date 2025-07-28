import streamlit as st

# 유튜브 영상 링크
url = 'https://www.youtube.com/watch?v=XyEOEBsa8I4'
#  추가 영상 링크 넣을거야 3개정도
url_paro = 'https://www.youtube.com/watch?v=eir-zqegNV8'
url_pepper = 'https://www.youtube.com/watch?v=iZhI5oD8zwM'
url_hd = 'https://www.youtube.com/watch?v=oiz6hyvTbXY'

# 페이지 기본 설정
st.set_page_config(layout='wide', page_title='EthicApp')

# 앱 타이틀
st.title('Ethic is good for us')

# # 사이드바 메뉴
# # (사이드바 버튼 추가): "학생데이터 가져오기" 버튼을 추가하고, 클릭했을 때, content영역에 저장된 학생 데이터(data.txt)를 불러와서 제시합니다.
# st.sidebar.subheader('Menu...')
# st.sidebar.markdown("""
# - AI 돌봄 로봇이란?
# - 윤리적 문제는?
# - 나의 생각은?
# """)

# 사이드바 메뉴
# (사이드바 버튼 추가): "학생데이터 가져오기" 버튼을 추가하고, 클릭했을 때, content영역에 저장된 학생 데이터(data.txt)를 불러와서 제시합니다.
st.sidebar.subheader('Menu...')
st.sidebar.markdown("""
- AI 돌봄 로봇이란?
- 윤리적 문제는?
- 나의 생각은?
""")

# 학생데이터 보기 버튼
show_data = st.sidebar.button("📂 학생데이터 가져오기")
# st.rerun()


# 화면 2개 컬럼 분할 (4:1 비율)
col1, col2 = st.columns((4, 1))

# 왼쪽 넓은 영역 - Content
with col1:
    st.header("👀 영상으로 보는 'AI 돌봄 로봇'")
    # (넘기기 버튼 추가)지금은 영상 하나만 있는데 추가해야될 내용이 영상 오른쪽, 왼쪽에 화살표를 넣어서 영상 여러개를 볼 수 있게 만들고 싶어 그리고 url주소는 위에 url_paro, url_pepper, url_hd 넣을거야
    st.video(url)

    # 영상 아래에 학생 의견 입력창 추가
    st.markdown("### ✍️ 나의 생각을 적어보세요")
    user_name = st.text_input("이름을 입력하세요", key="name")
    user_opinion = st.text_area("영상을 보고 떠오른 생각이나 의견을 자유롭게 작성해보세요", key="opinion")
    submit = st.button("제출하기")

    if submit:
        if user_name.strip() == "" or user_opinion.strip() == "":
            st.warning("이름과 의견을 모두 입력해주세요.")
        else:
            with open("./data/data.txt", "a", encoding="utf-8") as f:
                f.write(f"[이름] {user_name}\n[의견] {user_opinion}\n{'-'*40}\n")
            st.success("의견이 성공적으로 제출되었습니다. 감사합니다!")
            # st.rerun()

    st.markdown("""
    ### 🤖 돌봄 로봇의 윤리
    - Pepper, Paro, 효돌이와 같은 AI 로봇이 인간을 어떻게 돌보는지 살펴보세요.
    - 돌봄은 따뜻함인가, 효율성인가?
    """)

        # 사이드바 버튼 클릭 시 학생 의견 불러오기
    if show_data:
        st.markdown("### 📋 제출된 학생 의견")
        try:
            with open("./data/data.txt", "r", encoding="utf-8") as f:
                student_data = f.read()
                if student_data.strip() == "":
                    st.info("아직 제출된 의견이 없습니다.")
                else:
                    st.text(student_data)
        except FileNotFoundError:
            st.error("data.txt 파일이 존재하지 않습니다.")


# 오른쪽 좁은 영역 - Tips
with col2:
    st.subheader("💡 Tips...")
    st.info("""
    ▸ 돌봄 로봇은 인간을 대신할 수 있을까요?  
    ▸ 감정을 인식하고 반응하는 AI는 인간과 같을까요?  
    ▸ 우리는 이 기술을 어떻게 바라보아야 할까요?
    """)

    st.markdown("---")
    st.write("👉 아래 영상은 수업 도입용으로 사용 가능합니다.")
