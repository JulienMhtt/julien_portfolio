import streamlit as st
from contants import *

st.set_page_config(page_title="Technical skills", layout = "wide", initial_sidebar_state = "auto")

# ---------- Sidebar ---------- #
st.sidebar.page_link("home.py", label="Home", icon="🏠")
st.sidebar.page_link("pages/experiences.py", label="Experiences", icon="🧐")
st.sidebar.page_link("pages/education.py", label="Education", icon="📚")
st.sidebar.page_link("pages/technical_skills.py", label="Technical Skills", icon="🛠️")
st.sidebar.page_link("pages/llm_prompt.py", label="LLM Prompt", icon="🤖")
st.sidebar.page_link("pages/portfolio.py", label="Portfolio", icon="📔")
#st.sidebar.page_link("pages/contact.py", label="Contact", icon="✉️")

# ---------- Contact ---------- #
comp_contact()

# ---------- LLM Prompt ----------#
st.title("🤖 LLM Prompt")
st.write("")
st.write("##### **In here I wanna share with you the prompts I'm using on a regular basis**")
st.write("")

# Prompt selection
prompt_names= ["Select a prompt"] + list(llm_prompt_info.keys())
selected_prompt = st.selectbox("Select a prompt", prompt_names, label_visibility="hidden")
st.write("")

# Display
if selected_prompt != "Select a prompt":
    st.subheader(selected_prompt, divider="grey")
    st.write("")
    st.write("")
    st.markdown(llm_prompt_info[selected_prompt]["description"], unsafe_allow_html=True)
    st.write("")
    st.code(llm_prompt_info[selected_prompt]["prompt"], language="text")