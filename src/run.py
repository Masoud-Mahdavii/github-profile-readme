import streamlit as st
from pathlib import Path

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
    github = col1.text_input("Github")
    linkedin = col2.text_input("Linkdin")
    twitter = col1.text_input("Twitter")
    facebook = col2.text_input("Facebook")
    instagram = col1.text_input("Instagram")
    youtube = col2.text_input("Youtube")
    medium = col1.text_input("Medium")


# Select Theme
st.header("Theme")
themes = Path("src/themes").iterdir()
themes = [theme.name for theme in themes]
theme =st.selectbox("Select Theme", themes)
st.markdown(f"Selected Theme: {theme}")


# Generate Readme
st.header("Generate Readme")