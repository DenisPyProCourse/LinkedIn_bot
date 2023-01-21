from os.path import join, dirname

import streamlit as st
import os
import openai
from dotenv import load_dotenv

try:
    dotenv_path = join(dirname(__file__), '../.env')
    load_dotenv(dotenv_path)
    api_key = os.getenv('API_KEY') if os.getenv('API_KEY') and len(os.getenv('API_KEY')) > 0 else ''
except:
    EnvironmentError("Please, add your api_key to .env")
    api_key = ''

def work_exp_auto(desc, api_key):
    openai.api_key = api_key
    response = openai.Completion.create(
    engine="davinci-instruct-beta",
    prompt=f"Write a short work experience description for LinkedIn profile using given words in list from {desc}\n\n",
    temperature=1,
    max_tokens=400,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6
    )
    return response


def work_exp_manual(desc, api_key):
    openai.api_key = api_key
    st.sidebar.title('DenDv')
    st.sidebar.text("@ LinkedIn builder")
    st.sidebar.title('Page Selection Menu')
    page = st.sidebar.radio("Select Required Feature", ('Work experience',))
    st.title('LinkedIn Work experience Generator')
    description = st.text_area("Enter your name", desc)
    if st.button("Generate Work experience!"):
        if description == "":
            st.error("Please enter your description")
        else:
            with st.spinner("Fetching response..."):
                response = openai.Completion.create(
                    engine="davinci-instruct-beta",
                    prompt=f"Write a short work experience description for LinkedIn profile using given words in list from {desc}\n\n",
                    temperature=1,
                    max_tokens=400,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0.6
                )
                st.markdown(response['choices'][0]['text'])
                return response



