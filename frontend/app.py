import streamlit as st
import requests

st.title("🚦 AI Traffic Management")

if st.button("Start Vehicle Detection"):
    response = requests.get("http://127.0.0.1:8000/detect/")
    st.write(response.json())

if st.button("Optimize Traffic Lights"):
    response = requests.get("http://127.0.0.1:8000/control/")
    st.write(response.json())
