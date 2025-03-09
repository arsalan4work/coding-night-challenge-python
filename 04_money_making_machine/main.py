import streamlit as st
import random
import time
import requests

# Streamlit App Title
st.title("💰 Money Making Machine 💰")

# Function to Generate Random Money Amount
def generate_money():
    return random.randint(1, 1000000)  # Generates a random amount between $1 and $1,000,000

# Money Generator Section
st.subheader("💸 Instant Cash Generator")
if st.button("🎰 Generate Money"):
    st.write("💵 Counting your money...")
    time.sleep(3)  # Simulating processing time
    amount = generate_money()
    st.toast("✅ Money Generated!")
    st.success(f"🎉 You made **${amount:,}**! 🤑")

# Function to Fetch Side Hustle Ideas
def fetch_side_hustle():
    try:
        response = requests.get('http://127.0.0.1:8000/side_hustles')
        if response.status_code == 200:
            hustles = response.json()
            return hustles["side_hustles: "]
        else:
            return "🚫 No side hustles found!"
    except:
        return "⚠️ Something Went Wrong! Please try again."

# Side Hustle Ideas Section
st.subheader("🚀 Side Hustle Ideas")
if st.button("💡 Generate Hustle"):
    idea = fetch_side_hustle()
    st.success(f"🛠️ Side Hustle Idea: {idea}")

# Function to Fetch Money Quotes
def fetch_money_quotes():
    try:
        res = requests.get('http://127.0.0.1:8000/money_quotes')
        if res.status_code == 200:
            quote = res.json()
            return quote["money_quotes: "] 
        else:
            return "🚫 No money quotes found!"
    except:
        return "⚠️ Something Went Wrong! Please try again."

# 💬 Money Quotes Section
st.subheader("💬 Money Quotes")
if st.button("📜 Generate Quotes"):
    quotes = fetch_money_quotes()
    st.success(f"💡 Money Wisdom: {quotes}")