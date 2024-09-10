import streamlit as st
from contants import *

st.set_page_config(page_title="Julien Mahiette", page_icon = "👨‍💻", layout = "wide", initial_sidebar_state = "auto")

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

# ---------- Title ---------- #
st.markdown(f"""
    ## Hi, I'm {info["Full_name"]}, welcome 👋
""")
st.write("")
st.write("")

# ---------- Description ---------- #
with st.container():
    col1, col2 = st.columns([2, 1], gap="large")

    with col1:
        st.subheader(info["Position"], divider="grey")
        st.markdown(info["Intro"], unsafe_allow_html=True)

    with col2:
        st.image(info["image"], width=200)

st.write("")
st.write("")
