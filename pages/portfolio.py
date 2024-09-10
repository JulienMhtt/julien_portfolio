import streamlit as st
from contants import *
from functions import *

st.set_page_config(layout = "wide")

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

# ---------- Portfolio ---------- #
st.title("📔 Portfolio")

tab1, tab2, tab3 = st.tabs(["DQM lite", "Filecheck", "Car sales performance"])

with tab1:
    st.write("")
    st.subheader("DQM lite", divider="grey")

    # Description
    st.markdown("""
                - **Purpose**:
                This app will be on the same base as my Filecheck app but more complete made with my latest expereinces in data quality. <br>
                The purpose stays the same

                 - **Reason**:
                Despite the criticism Excel often receives, it remains the top tool for non-IT services because it is widely used and user-friendly. <br>
                This tool can help these services check their file quality without needing programming skills, <br>
                as it is everyone's responsibility to avoid spreading incorrect data. <br>
                Furthermore, it can serve as an introduction to data for them and assist the company in succeeding in its data transformation efforts.
                """,
                unsafe_allow_html=True)
    
    # DQM lite
    st.title("COMING UP SOON!")


with tab2:
    st.write("")
    st.subheader("Filecheck App", divider="grey")

    # Description
    st.markdown("""
                - **Purpose**:
                This app is designed to help me and others quickly check the quality of CSV or XLSX files we receive. <br>
                Sometimes, when querying a database, we lack visibility; therefore, exporting the result as a CSV and using this tool can help identify inconsistencies. <br>
                Even though Data Engineers do great work, we should always verify the data 😇.

                 - **Reason**:
                Despite the criticism Excel often receives, it remains the top tool for non-IT services because it is widely used and user-friendly. <br>
                This tool can help these services check their file quality without needing programming skills, <br>
                as it is everyone's responsibility to avoid spreading incorrect data. <br>
                Furthermore, it can serve as an introduction to data for them and assist the company in succeeding in its data transformation efforts.

                - **Link**:
                https://filecheck.streamlit.app
                """,
                unsafe_allow_html=True)
    st.write("")
    st.write("")

    # Filecheck            
    for index, portefolio_section in enumerate(portfolio_info["filecheck"]):
        column_layout1 = [3, 1]
        column_layout2 = [1, 3]
        column_layout = column_layout1 if index % 2 == 0 else column_layout2

        item1 = portfolio_info["filecheck"][portefolio_section]["image"]
        item2 = portfolio_info["filecheck"][portefolio_section]["description"]

        portfolio_container(column_layout, item1, item2)
        st.write("")
        st.write("")

with tab3:
    st.write("")
    st.subheader("Car sales performance", divider="grey")

    # Description
    st.markdown("""
                - **Purpose**: <br>
                This small project was developed to showcase my Power BI skills.

                - **Problem statement**: <br>
                I am working for a large, multi-brand car sales company in the United States. <br>
                The CEO wants a dashboard to monitor the company's overhall performance. <br>
                He also wants to give state CEOs access to the dashboard, allowing them to monitor individual dealerships in their state with greater detail. <br>

                - **Extra info**: <br>
                I aimed for a minimalist approach, removing redundant elements and using color sparingly. <br>
                The dataset is limited to 2014 and 2015, with many states and dealerships lacking sufficient data. <br>
                While additional data like US demographics and income levels could be added, that is not the purpose of this project.
                """,
                unsafe_allow_html=True)
    st.write("")
    st.write("")

    # Car sales performance
    for index, portefolio_section in enumerate(portfolio_info["car_sales_performance"]):
        column_layout1 = [3, 1]
        column_layout2 = [1, 3]
        column_layout = column_layout1 if index % 2 == 0 else column_layout2

        item1 = portfolio_info["car_sales_performance"][portefolio_section]["image"]
        item2 = portfolio_info["car_sales_performance"][portefolio_section]["description"]

        portfolio_container(column_layout, item1, item2)
        st.write("")
        st.write("")

