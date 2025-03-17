import streamlit as st
import requests

def random_joke_generator():
    """ Fetch a random joke from an external API."""
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        
        if response.status_code == 200:
            jokes_data = response.json()
            return f"{jokes_data['setup']} \n\n {jokes_data['punchline']}"
        else:
            return "Failed to fetch API! Please try again later."
    except Exception as e:
        st.error(f"An error occurred: {e}")

def main():
    """
    Main function to render the Streamlit app.
    """
    st.title("🎃 Random Jokes Generator") 
    st.write("Click the button below to generate a random joke!")

    # Button to fetch and display a random joke
    if st.button("Generate Joke"):
        joke = random_joke_generator()
        st.write(joke)
    
    st.divider()

    # Footer section with attribution
    st.markdown("""
    <div style='text-align:center; color:gray;'>
        <p>Random Jokes Generator</p>
        <p>Built with ❤ by <a href='https://github.com/arsalan4work'>Muhammad Arsalan</a></p>
    </div>
    """, unsafe_allow_html=True)
    
if __name__ == "__main__":
    main()
