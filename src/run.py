import streamlit as st

st.title(":zap: Github Profile Readme")


# personal(info)
st.header("Personal Info")
with st.expander("Personal Info"):
    col1, col2 = st.columns(2)
    name = col1.text_input("Name")
    homepage = col2.text_input("Homepage")
    location = st.text_input("Location")
    email = col2.text_input("Email")
    phone = col1.text_input("Phone")


# Social Media

st.header("Social Media")
with st.expander("Social Media"):
    col1, col2 = st.columns(2)
    
