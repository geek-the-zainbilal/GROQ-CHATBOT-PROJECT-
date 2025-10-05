import os
import streamlit as st
from dotenv import load_dotenv
from main import compiled_graph

load_dotenv()

# ---------- UI Title ----------
st.title("🤖 GROQ AI CHATBOT CREATED BY - MALIK ZAIN")

# ---------- API Key Input ----------
if "api_key" not in st.session_state:
    st.session_state.api_key = ""

st.session_state.api_key = st.text_input(
    "Enter your GROQ API Key:",
    type="password",
    value=st.session_state.api_key,
    placeholder="Paste your Groq API key here..."
)

# ---------- Validation ----------
if not st.session_state.api_key:
    st.warning("Please enter your Groq API key to continue.")
    st.stop()  # Stops the app here until key is entered

os.environ["GROQ_API_KEY"] = st.session_state.api_key

# ---------- Chat Section ----------
user_input = st.text_input("ENTER PROMPT HERE")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Run the LLM
    output = compiled_graph.invoke({"user_message": user_input})
    bot_reply = output["bot_message"]
    
    # Add bot response
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    
    # Display immediately
    with st.chat_message("assistant"):
        st.markdown(bot_reply)
