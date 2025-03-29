import streamlit as st
import streamlit.components.v1 as components

with open("dashboard.html", "r", encoding="utf-8") as f:
    html_string = f.read()

components.html(
    html_string,
    height=1000,  # You can increase this if needed, or make it responsive below
    width=2000
)
