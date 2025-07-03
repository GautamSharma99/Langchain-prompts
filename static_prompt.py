from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
import os
load_dotenv()
api_key = os.getenv("OPENAI_KEY")

model = ChatOpenAI(model='gpt-4o-mini'
                   ,api_key=api_key)

st.header('Research Tool')

user_input = st.text_input('enter your prompt')

if st.button('summarise'):
    result = model.invoke(user_input)
    st.write(result.content)