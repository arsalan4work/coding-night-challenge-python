import streamlit as st
import random
import string

# Function to generate a secure password
def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters  # Add ASCII Letters (A-Z, a-z)
    
    if use_digits:
        characters += string.digits  # Add digits (0-9)
    
    if use_special:
        characters += string.punctuation  # Add special characters (!@#$%^&* etc.)
    
    return "".join(random.choice(characters) for _ in range(length))  # Generate password

# Streamlit UI
st.title("🔐 Password Generator")

# Slider to select password length
length = st.slider("📏 Select Password Length", min_value=8, max_value=32, value=12) 

# Checkboxes to include digits and special characters
use_digits = st.checkbox("🔢 Include Digits")
use_special = st.checkbox("✨ Include Special Characters")

# Button to generate the password
if st.button("Generate Now"):
    password = generate_password(length, use_digits, use_special)
    st.write(f"✅ Generated Password: `{password}`")

# Footer section
st.write("---")
st.write("💡 Built with ❤️ by [Muhammad Arsalan](https://github.com/arsalan4work)")