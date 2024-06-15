import streamlit as st

st.metric(label="Gas price", value=4, delta=-0.5,
    delta_color="inverse")

st.metric(label="Active developers", value=123, delta=123,
    delta_color="off")
    
st.title('동물 이미지 찾아주기 😎')

name = st.text_input('영어로 동물을 입력하세요')

if st.button('찾아보기'):
    st.image(f'https://edu.spartacodingclub.kr/random/?{name}')