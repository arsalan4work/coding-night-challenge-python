import streamlit as st

st.title("Simple Streamlit App")

user_input = st.text_input("Enter your name: ")

if st.button("Show Message"):
   st.write(f"Your Name is: {user_input}")