import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile"
)

st.title("AI Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    role = "user" if isinstance(msg, HumanMessage) else "assistant"
    st.chat_message(role).write(msg.content)

user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append(HumanMessage(content=user_input))
    response = llm.invoke(st.session_state.messages)
    st.session_state.messages.append(AIMessage(content=response.content))
    st.rerun()