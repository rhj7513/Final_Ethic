import streamlit as st
st.title('This is my first webapp!!')
st.info('이 앱은 윤리가 고려된 인공지능융합수업의 일환으로 개발되었습니다.')
col1, col2 = st.columns((4,1))
with col1:
    with st.expander('Content...'):
        import pandas as pd
        df = pd.read_csv('./data/mydata.csv')
        st.write(df)

with col2:
    with st.expander('Tips...'):
        pass