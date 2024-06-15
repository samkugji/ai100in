import os
import streamlit as st
from openai import OpenAI

client = OpenAI(
    api_key=st.secrets["API_KEY"]
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "이미지 url을 받아서 화면에 보여주는 파이썬 코딩을 써줘",
        }
    ],
    model="gpt-4o",
)

st.write(chat_completion.choices[0].message.content)
