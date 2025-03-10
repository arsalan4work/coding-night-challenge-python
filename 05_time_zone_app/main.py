# Import required libraries
import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

# List of available time zones
TIME_ZONES = [
    "UTC",
    "Asia/Karachi",
    "America/New_York",
    "Europe/London",
    "Asia/Tokyo",
    "Australia/Sydney",
    "America/Los_Angeles",
    "Europe/Berlin",
    "Asia/Dubai",
    "Asia/Kolkata",
]

# Time Zone Application
st.title("🕒 Time Zone App 🌍")

# Allow users to select multiple time zones for display
selected_timezone = st.multiselect("Select Timezones", TIME_ZONES, default=["UTC", "Asia/Karachi"])

# Display the current time for selected time zones
st.subheader("⏳ Selected Timezones")
for tz in selected_timezone:
    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    st.write(f"**{tz}**: {current_time}")

# Time conversion feature between different time zones
st.subheader("🔄 Convert Time Between Timezones")

# Allow users to select a specific time to convert
current_time = st.time_input("Select Current Time", value=datetime.now().time())

# Drop-down menus for selecting the source and target time zones
from_tz = st.selectbox("From Timezone", TIME_ZONES, index=0)
to_tz = st.selectbox("To Timezone", TIME_ZONES, index=1)

# Button to perform time conversion
if st.button("Convert Time"):
    # Combine the selected time with today's date and apply the selected time zone
    dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_tz))
    
    # Convert the selected time to the target time zone
    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    
    # Display the converted time with custom css styling
    st.markdown(
        f"""
        <div style="background-color: #f8f9fa; padding: 10px; border-radius: 10px; color: #212529; text-align: center;">
            <h3>🌟 Time Converted! 🕒</h3>
            <p><b>In {to_tz}, it's now {converted_time} 🎉</b></p>
        </div>
        """, unsafe_allow_html=True
    )