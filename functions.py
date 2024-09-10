import streamlit as st

# Container layout
def portfolio_container(column_layout, item1, item2):
    with st.container(border=True):
        col1, col2 = st.columns(column_layout, gap="large", vertical_alignment="center")

        with col1:
            if column_layout == [3, 1]:
                st.image(item1)
            else:
                st.markdown(item2, unsafe_allow_html=True)
        
        with col2:
            if column_layout == [3, 1]:
                st.markdown(item2, unsafe_allow_html=True)
            else:
                st.image(item1)
    st.write("")