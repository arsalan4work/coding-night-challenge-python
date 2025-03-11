import streamlit as st  # Web UI
import pandas as pd  # Data manipulation
import datetime  # Handling dates
import csv  # Reading/writing CSV
import os  # File operations

# Define the file name for storing mood data
MOOD_FILE = "mood_log.csv"

# Function to ensure the CSV file exists with headers
def ensure_csv_file():
    if not os.path.exists(MOOD_FILE) or os.stat(MOOD_FILE).st_size == 0:
        with open(MOOD_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Mood"])  # Ensure column headers exist

# Function to load mood data
def load_mood_data():
    ensure_csv_file()
    try:
        return pd.read_csv(MOOD_FILE, encoding="utf-8")
    except pd.errors.EmptyDataError:
        return pd.DataFrame(columns=["Date", "Mood"])

# Function to get the next available date
def get_next_date():
    data = load_mood_data()
    
    if data.empty:
        return datetime.date(2025, 1, 1)  # Start from 1st Jan 2025
    
    last_date = pd.to_datetime(data["Date"]).max().date()
    return last_date + datetime.timedelta(days=1)  # Increment by 1 day

# Function to add a new mood entry
def save_mood_data(mood):
    next_date = get_next_date()  # Get the next available date
    with open(MOOD_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([next_date, mood])

# 🌟 Streamlit App Title
st.title("📝 Mood Tracker")

# Subheader for user input
st.subheader("😃 How are you feeling today?")

# Dropdown for mood selection
mood = st.selectbox("Select your mood", ["Happy 😊", "Sad 😢", "Angry 😡", "Neutral 😐", "Excited 🤩", "Anxious 😰", "Grateful 🙏"])

# Button to save mood
if st.button("Log Mood"):
    save_mood_data(mood)  # Save the mood to CSV
    st.success(f"✅ Mood Logged Successfully: {mood}")  # Confirmation
    st.rerun()  # Refresh app to update history instantly

# Load existing mood data
data = load_mood_data()

# Display mood history only if data exists
if not data.empty:
    st.subheader("📊 Mood Trends Over Time")
    
    # Convert 'Date' column to datetime for proper processing
    data["Date"] = pd.to_datetime(data["Date"])
    
    # Count occurrences of each mood
    mood_counts = data.groupby("Mood").count()["Date"]
    
    # Display bar chart of mood frequencies
    st.bar_chart(mood_counts)
    
    # Display raw data
    st.subheader("📅 Your Mood History")
    st.dataframe(data.sort_values(by="Date", ascending=False), use_container_width=True)

# Footer with credit
st.write("🚀 Built with ❤️ by Asharib Ali")
