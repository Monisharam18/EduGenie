import streamlit as st
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="EduGenie",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 EduGenie")
st.subheader("Google Gemini Powered Learning Assistant")

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("Gemini API key is missing. Please add it to the .env file.")
    st.stop()

client = genai.Client(api_key=api_key)

question = st.text_area(
    "Ask EduGenie anything about your studies:",
    placeholder="Example: Explain Python loops in simple words."
)

if st.button("Ask EduGenie 🤖"):
    if question.strip():
        with st.spinner("EduGenie is thinking..."):
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=f"""
You are EduGenie, a helpful learning assistant for BCA college students.
Explain concepts clearly and simply.
Use examples when useful.

Student question:
{question}
"""
            )

            st.markdown("### 📚 EduGenie Answer")
            st.write(response.text)
    else:
        st.warning("Please enter a question.")