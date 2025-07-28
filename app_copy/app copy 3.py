import streamlit as st
import pandas as pd
import plotly.express as px

# 제목 및 정보
st.title('This is my first webapp!!')
st.info('이 앱은 윤리가 고려된 인공지능융합수업의 일환으로 개발되었습니다.')

# CSV 파일 읽기
df = pd.read_csv('./data/mydata.csv')

# 총점, 평균, 등급 계산
df['total'] = df[['kor', 'eng', 'math']].sum(axis=1)
df['average'] = df['total'] / 3

# 등급 함수 정의
def grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 70:
        return 'B'
    else:
        return 'C'

df['grade_level'] = df['average'].apply(grade)

# 컬럼 구성
col1, col2 = st.columns((4, 1))

# 왼쪽 컬럼: 콘텐츠 영역
with col1:
    with st.expander('Content...'):
        st.subheader('📊 학생 성적 테이블')
        st.dataframe(df)

        # 과목별 점수 막대그래프
        st.subheader('📌 과목별 점수 분포 (막대그래프)')
        df_melt = df.melt(id_vars=['name'], value_vars=['kor', 'eng', 'math'],
                          var_name='subject', value_name='score')
        fig1 = px.bar(df_melt, x='name', y='score', color='subject', barmode='group',
                      labels={'name': '학생 이름', 'score': '점수', 'subject': '과목'})
        st.plotly_chart(fig1, use_container_width=True)

        # 평균 점수 꺾은선그래프
        st.subheader('📈 평균 점수 변화 (꺾은선 그래프)')
        fig2 = px.line(df, x='name', y='average', markers=True,
                       labels={'name': '학생 이름', 'average': '평균 점수'})
        st.plotly_chart(fig2, use_container_width=True)

        # 등급별 비율 파이차트
        st.subheader('🥧 등급별 학생 비율 (파이 차트)')
        grade_counts = df['grade_level'].value_counts().reset_index()
        grade_counts.columns = ['grade', 'count']
        fig3 = px.pie(grade_counts, names='grade', values='count', hole=0.3,
                      title='등급별 비율')
        st.plotly_chart(fig3, use_container_width=True)

# 오른쪽 컬럼: 팁 제공 영역
with col2:
    with st.expander('Tips...'):
        st.markdown('''
        ### 📘 과목별 평가 기준
        - **국어**
          - A: 90점 이상 (문해력 우수)
          - B: 70~89점 (기본적 이해)
          - C: 70점 미만 (보완 필요)

        - **영어**
          - A: 90점 이상 (의사소통 능력 우수)
          - B: 70~89점 (기초 회화 가능)
          - C: 70점 미만 (기초 부족)

        - **수학**
          - A: 90점 이상 (문제해결력 우수)
          - B: 70~89점 (개념 이해 가능)
          - C: 70점 미만 (기초 부족)
        ''')
