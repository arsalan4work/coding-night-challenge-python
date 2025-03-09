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
      response = requests.get('http://127.0.0.1:8000/side_hustles')
      if response.status_code == 200:
        hustles = response.json()
        return hustles["side_hustles: "]
      else:
         return("No side hustles found!")
    except:
      return("Something Went Wrong!")
    
st.subheader("Side Hustle Ideas")

if st.button("Generate Hustle"):
   idea = fetch_side_hustle()
   st.success(idea)


def fetch_money_quotes():
   try:
      res = requests.get('http://127.0.0.1:8000/money_quotes')
      if res.status_code == 200:
         quote = res.json()
         return quote["money_quotes: "]
      else:
         return("No money quotes found!")
   except:
      return("Something Went Wrong!")

st.subheader("Money Quotes Ideas")
if st.button("Generate Quotes"):
   quotes = fetch_money_quotes()
   st.success(quotes)