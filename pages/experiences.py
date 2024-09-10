import streamlit as st
from contants import *

st.set_page_config(page_title="Experiences", layout = "wide", initial_sidebar_state = "auto")

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

# ---------- Experiences ----------#
st.title("🧐 Experiences")
st.write("")
st.write("For the sake of clarity, I removed some short experiences")
st.write("")


def experience_layout(job, company, contract, period, logo, what, country):

    with st.container(border=True):
        st.subheader(f"""
                        {job} - {company} - {country} 
                        _{contract}_ / _{period}_ 
                    """
                    ,  divider="grey")
        
        col1, col2, col3 = st.columns([1, 0.5, 6], vertical_alignment="center")

        with col1:
            st.image(logo)
        
        with col2:
            st.empty()

        with col3:
            st.markdown(what, unsafe_allow_html=True)
        
        st.write("")
    st.write("")
    st.write("")

tab1, tab2, tab3 = st.tabs(["Data", "France", "Abroad"])


for experience in experience_info:
    if experience_info[experience]["tab"] == "Data":
        with tab1:
            experience_layout(experience_info[experience]["job"], experience_info[experience]["company"], 
                              experience_info[experience]["contract"], experience_info[experience]["period"],
                              experience_info[experience]["logo"], experience_info[experience]["what"],
                              experience_info[experience]["country"])

    if experience_info[experience]["tab"] == "France":
        with tab2:
            experience_layout(experience_info[experience]["job"], experience_info[experience]["company"], 
                              experience_info[experience]["contract"], experience_info[experience]["period"],
                              experience_info[experience]["logo"], experience_info[experience]["what"],
                              experience_info[experience]["country"])

    if experience_info[experience]["tab"] == "Abroad":
        with tab3:
            experience_layout(experience_info[experience]["job"], experience_info[experience]["company"], 
                              experience_info[experience]["contract"], experience_info[experience]["period"],
                              experience_info[experience]["logo"], experience_info[experience]["what"],
                              experience_info[experience]["country"])



