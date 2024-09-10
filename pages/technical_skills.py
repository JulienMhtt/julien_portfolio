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

# ---------- Technical skills ---------- #
st.title("🛠️ Technical skills")
st.write("")
st.write("")

# Programming languages
st.subheader("Programming languages", divider="grey")
st.markdown("""
            - Python:
                - Collecting, cleaning and analysing data.
                - Building tools.
            """,
            unsafe_allow_html=True)
st.write("")

# Query language
st.subheader("Query language", divider="grey")
st.markdown("""
            - SQL:
                - Writting queries for extraction, transformation and analysis.
            """,
            unsafe_allow_html=True)
st.write("")

# Data analysis and visualization
st.subheader("Data analysis and visualization", divider="grey")
st.markdown("""
            - Pandas:
                - Data manipulation and analysis.
            
            <br>

            - Plotly:
                - Creating interactive data visualization.
            
            <br>

            - Streamlit:
                - Building interactive web application and dashboards.
            """,
            unsafe_allow_html=True)
st.write("")

# Reporting tools
st.subheader("Reporting tools", divider="grey")
st.markdown("""
            - Power BI:
                - Creating detailed reports and dashboards.
            
            <br>

            - DAX:
                - Data Analysis Expressions for complex calculations.
            
            <br>

            - Power Query:
                - Data transformation and connection.
            """,
            unsafe_allow_html=True)
st.write("")

# Data engineering
st.subheader("Data engineering", divider="grey")
st.markdown("""
            - AWS services:
                - S3: Data lake storage.
                - Glue: Managed ETL service.
                - Crawler: Automatic schema discovery.
            
            <br>

            - Open Source Tools:
                - Apache Airflow: Workflow automation and scheduling.
                - DBT: Data transformation and modeling.
            """,
            unsafe_allow_html=True)
st.write("")
