import streamlit as st
from contants import *

st.set_page_config(page_title="Education", layout = "wide", initial_sidebar_state = "auto")

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

# ---------- Education ----------#
st.title("📚 Education")
st.write("")
st.write("")

# All the certification and degrees
for education in education_info:
    with st.container(border=True):
        st.subheader(f"""
                        {education_info[education]["degree"]}
                        _{education_info[education]["school"]}_ / _{education_info[education]["when"]}_
                    """,
                      divider="grey")

        col1, col2, col3 = st.columns([1, 0.5, 6])

        with col1:
            st.image(education_info[education]["logo"], width=150)

        with col2:
            st.empty()

        with col3:
            st.markdown(education_info[education]["what"])
    st.write("")
    st.write("")
