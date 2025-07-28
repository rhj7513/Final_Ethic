import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 제목 및 설명
st.title('This is my first webapp!!')
st.info('이 앱은 윤리가 고려된 인공지능융합수업의 일환으로 개발되었습니다.')

# 데이터 로드
df = pd.read_csv('./data/mydata.csv')

# 점수 계산
df['total'] = df[['kor', 'eng', 'math']].sum(axis=1)
df['average'] = df['total'] / 3

# 등급 부여 함수
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

# 좌측: 데이터 테이블 및 시각화
with col1:
    with st.expander('Content...'):
        st.subheader('학생 성적 테이블')
        st.dataframe(df)

        st.subheader('과목별 점수 분포 (막대그래프)')
        fig1, ax1 = plt.subplots()
        df.set_index('name')[['kor', 'eng', 'math']].plot(kind='bar', ax=ax1)
        st.pyplot(fig1)

        st.subheader('학생별 평균 점수 (꺾은선 그래프)')
        fig2, ax2 = plt.subplots()
        ax2.plot(df['name'], df['average'], marker='o')
        ax2.set_ylabel('평균 점수')
        st.pyplot(fig2)

        st.subheader('등급별 학생 비율 (파이 차트)')
        grade_counts = df['grade_level'].value_counts()
        fig3, ax3 = plt.subplots()
        ax3.pie(grade_counts, labels=grade_counts.index, autopct='%1.1f%%', startangle=90)
        ax3.axis('equal')
        st.pyplot(fig3)

# 우측: 평가 기준
with col2:
    with st.expander('Tips...'):
        st.markdown('''
        ### 📘 과목별 평가 기준
        - **국어**
          - 90점 이상: A (문해력 우수)
          - 70~89점: B (기본적 이해 가능)
          - 70점 미만: C (보완 필요)

        - **영어**
          - 90점 이상: A (의사소통 능력 우수)
          - 70~89점: B (기본 회화 가능)
          - 70점 미만: C (기초 부족)

        - **수학**
          - 90점 이상: A (문제 해결 능력 우수)
          - 70~89점: B (기초 개념 이해)
          - 70점 미만: C (연산력 및 개념 부족)
        ''')

