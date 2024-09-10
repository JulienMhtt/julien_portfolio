import streamlit as st
from contants import *

st.set_page_config(page_title="Contact", layout = "wide", initial_sidebar_state = "auto")

# ---------- Sidebar ---------- #
st.sidebar.page_link("home.py", label="Home", icon="🏠")
st.sidebar.page_link("pages/experiences.py", label="Experiences", icon="🧐")
st.sidebar.page_link("pages/education.py", label="Education", icon="📚")
st.sidebar.page_link("pages/technical_skills.py", label="Technical Skills", icon="🛠️")
st.sidebar.page_link("pages/llm_prompt.py", label="LLM Prompt", icon="🤖")
st.sidebar.page_link("pages/portfolio.py", label="Portfolio", icon="📔")
st.sidebar.page_link("pages/contact.py", label="Contact", icon="✉️")

# ---------- Contact ---------- #
st.title("✉️ Contact")
st.write("")
st.write("")

with st.container():
    col1, col2 = st.columns([2, 1], gap="large")

    with col1: 
        st.header(contact_info["Full_name"], divider="grey")
        st.write("")

        col3, col4, col5= st.columns([2, 0.1, 2.5])
        with col3:
            st.subheader("✆ Phone number:")
            st.subheader("＠ Email address:")
            st.subheader("LinkedIn:")
        
        with col4:
            st.empty()

        with col5:
            st.subheader(f"_{contact_info["Phone_number"]}_")
            st.subheader(f"_{contact_info["Email"]}_")
            st.subheader(f"_{contact_info["LinkedIn"]}_")

    with col2:
        st.image(info["image"], width=200)

