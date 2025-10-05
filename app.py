from main import compiled_graph
import streamlit as st
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Title
st.title("🤖 GROQ AI CHATBOT - by Malik Zain")

# Initialize history if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input box
user_input = st.chat_input("Type your message...")

# When user sends a message
if user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Invoke chatbot
    response = compiled_graph.invoke({"user_message": user_input})
    bot_reply = response["bot_message"]

    # Add bot reply
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

    # Display the new reply instantly
    with st.chat_message("assistant"):
        st.markdown(bot_reply)

