import streamlit as st
import random
import time
import requests

st.title("Money Making Machine")

def generate_money():
   return random.randint(1,1000000)

st.subheader("Instant Cash Generator")
if st.button("Generate Money"):
   st.write("Counting your money...")
   time.sleep(5)
   amount = generate_money()
   st.toast("Money Generated!")
   st.success(f"You made ${amount}!")

def fetch_side_hustle():
    try:
      response = requests.get("https://127.0.0.1:8000/side_hustle")
      if response.status_code == 200:
        hustles = response.json()
        return hustles
      else:
         return("No side hustles found!")
    except:
      return("Something Went Wrong!")
    
st.subheader("Side Hustle Ideas")

if st.button("Generate Hustle"):
   idea = fetch_side_hustle()
   st.success(idea)