import streamlit as st
url='https://www.youtube.com/watch?v=XyEOEBsa8I4'

# 페이지 기본 설정
st.set_page_config(layout='wide', page_title='EthicApp')

# 앱 타이틀
st.title('Ethic is good for us')

# 사이드바 메뉴
st.sidebar.subheader('Menu...')
st.sidebar.markdown("""
- AI 돌봄 로봇이란?
- 윤리적 문제는?
- 나의 생각은?
""")

# 화면 2개 컬럼 분할 (4:1 비율)
col1, col2 = st.columns((4, 1))

# 왼쪽 넓은 영역 - Content
with col1:
    st.header("👀 영상으로 보는 'AI 돌봄 로봇'")
    st.video(url)  # 예시 영상. 필요시 다른 영상 URL로 교체 가능
    #(코드 추가 요청 주석): 영상 바로 아라에 학생들의 개인적인 생각을 기록하는 부분을 포함하고, 제출하기 버튼을 클릭하면, data.txt에 append되도록 합니다.
    st.markdown("""
    ### 🤖 돌봄 로봇의 윤리
    - Pepper, Paro, 효돌이와 같은 AI 로봇이 인간을 어떻게 돌보는지 살펴보세요.
    - 돌봄은 따뜻함인가, 효율성인가?
    """)

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
