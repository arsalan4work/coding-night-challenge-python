import streamlit as st
import random
import time

# Title of the Streamlit App
st.title("🐍 Python Interviewer App")

# List of Expert-Level Python Interview Questions
questions = [
    {
        "question": "What is Python?",
        "options": [
            "A type of snake",
            "A programming language",
            "A database software",
            "A text editor"
        ],
        "answer": "A programming language"
    },
    {
        "question": "Which data type is used to store a sequence of characters in Python?",
        "options": [
            "int",
            "float",
            "string",
            "boolean"
        ],
        "answer": "string"
    },
    {
        "question": "How do you start a comment in Python?",
        "options": [
            "// This is a comment",
            "# This is a comment",
            "/* This is a comment */",
            "-- This is a comment"
        ],
        "answer": "# This is a comment"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": [
            "function",
            "define",
            "def",
            "fn"
        ],
        "answer": "def"
    },
    {
        "question": "What is used to store multiple values in a single variable in Python?",
        "options": [
            "List",
            "Dictionary",
            "Tuple",
            "All of the above"
        ],
        "answer": "All of the above"
    },
    {
        "question": "Which of the following is NOT a valid Python data type?",
        "options": [
            "List",
            "Array",
            "Tuple",
            "Dictionary"
        ],
        "answer": "Array"
    },
    {
        "question": "Which function is used to display output in Python?",
        "options": [
            "echo()",
            "print()",
            "display()",
            "show()"
        ],
        "answer": "print()"
    },
    {
        "question": "Which loop in Python executes at least once even if the condition is false?",
        "options": [
            "for loop",
            "while loop",
            "do-while loop",
            "None of the above"
        ],
        "answer": "None of the above"
    },
    {
        "question": "What will be the output of `print(2 ** 3)` in Python?",
        "options": [
            "5",
            "6",
            "8",
            "9"
        ],
        "answer": "8"
    },
    {
        "question": "How do you take user input in Python?",
        "options": [
            "input()",
            "scan()",
            "get()",
            "read()"
        ],
        "answer": "input()"
    }
]

#  Initialize session state to store the current question
if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)

question = st.session_state.current_question

# Display the current question
st.subheader(question["question"])

# Radio button for selecting an answer
selected_options = st.radio("Choose your answer", question["options"], key="answer")

# Button to submit the answer
if st.button("Submit Answer"):
    if selected_options == question["answer"]:
        st.success("✅ Correct!")
        st.balloons()  # 🎈 Celebration animation
    else:
        st.error(f"❌ Incorrect! The correct answer is: {question['answer']}")
    
    time.sleep(3)  # Small delay before the next question
    
    # Load a new random question and refresh the app
    st.session_state.current_question = random.choice(questions)
    st.rerun()