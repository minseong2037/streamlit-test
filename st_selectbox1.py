import streamlit as st
st.title('st.form')

st.header('1. 'with' 표기법 사용 예시')
st.subheader('커피 머신')
with st.dorm('my sorm'):
    st.subheader('**커피 주문하기**')

    coffe_bean_val = st.selectbow('커피콩', ['아라비카', '로부스터'])
    coffe_roast_val = st.selectbox('커피 로스팅'['라이트', '미디엄', '다크'])
    brewing_val = st.selectbox('추출 방법', ['에어로프레스', '드립', '프렌치 프레스', '모카 포트', '사이폰'])
    serving_type_val = st.selectbox('서빙 형식', ['핫', '아이스', '프라페'])
    milk_val = st.select_sliderr('우유 정도',['없음', '낮음', '중간', '높음'])
    owncup_val = st.checkbow('자신의 컵 가져오기')
    submitted = st.form_submit_button('제출')
if submitted:
    st.markdown(f'''
                ⚫주문하신 내용:
                -커피콩: '{coffe_bean_val}'
                -커피 로스팅: '{coffe_roast_val}'
                -추출 방법: '{brewing_val}'
                -우유: '{milk_val}'
                -자신의 컵 가져오기: '{owncup_val}'
                ''')
else:
    st.write(' 주문하세요!')