import streamlit as st
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="EduGenie",
    page_icon="🎓",
    layout="wide"
)

# ---------------- HEADER ----------------
st.title("🎓 EduGenie")
st.subheader("Google Gemini Powered Learning Assistant")

st.markdown(
    "Your smart learning companion for BCA students."
)

st.divider()

# ---------------- SIDEBAR ----------------
st.sidebar.title("📚 EduGenie Menu")

menu = st.sidebar.radio(
    "Choose a section",
    [
        "🏠 Dashboard",
        "📚 Subjects",
        "📖 Study Materials",
        "📝 Quiz",
        "🤖 AI Study Assistant",
        "📊 Progress"
    ]
)

# ---------------- SUBJECTS ----------------
subjects = [
    "🐍 Python",
    "💻 C++",
    "🗄️ Database Management",
    "🌐 Web Technology",
    "📊 Data Structures",
    "🤖 Artificial Intelligence"
]

# ---------------- DASHBOARD ----------------
if menu == "🏠 Dashboard":

    st.header("👋 Welcome to EduGenie!")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("📚 Subjects", "6")

    with col2:
        st.metric("📖 Study Materials", "12+")

    with col3:
        st.metric("📝 Quiz Questions", "20+")

    st.markdown("### 🚀 What can you do?")

    st.info(
        "📚 Explore subjects\n\n"
        "📖 Access study materials\n\n"
        "📝 Practice quizzes\n\n"
        "🤖 Ask the AI Study Assistant\n\n"
        "📊 Track your learning progress"
    )

# ---------------- SUBJECTS ----------------
elif menu == "📚 Subjects":

    st.header("📚 Subjects")

    cols = st.columns(3)

    for i, subject in enumerate(subjects):
        with cols[i % 3]:
            st.button(
                subject,
                use_container_width=True
            )

# ---------------- STUDY MATERIALS ----------------
elif menu == "📖 Study Materials":

    st.header("📖 Study Materials")

    materials = {
        "🐍 Python": [
            "Python Basics",
            "Variables and Data Types",
            "Conditional Statements",
            "Loops",
            "Functions"
        ],
        "💻 C++": [
            "C++ Basics",
            "Variables",
            "Functions",
            "Classes and Objects",
            "Inheritance"
        ],
        "🗄️ Database Management": [
            "Database Basics",
            "SQL",
            "Keys",
            "Normalization",
            "Transactions"
        ],
        "🌐 Web Technology": [
            "HTML",
            "CSS",
            "JavaScript",
            "Web Forms",
            "Web Applications"
        ],
        "📊 Data Structures": [
            "Arrays",
            "Linked Lists",
            "Stacks",
            "Queues",
            "Searching and Sorting"
        ],
        "🤖 Artificial Intelligence": [
            "AI Basics",
            "Machine Learning",
            "Generative AI",
            "Neural Networks",
            "AI Applications"
        ]
    }

    selected_subject = st.selectbox(
        "Select a subject",
        list(materials.keys())
    )

    st.markdown("### 📌 Available Topics")

    for topic in materials[selected_subject]:
        st.checkbox(topic)

# ---------------- QUIZ ----------------
elif menu == "📝 Quiz":

    st.header("📝 Quick Quiz")

    st.write("Test your basic programming knowledge!")

    q1 = st.radio(
        "1. Which keyword is used to define a function in Python?",
        ["function", "def", "fun", "define"]
    )

    q2 = st.radio(
        "2. Which data structure follows LIFO?",
        ["Queue", "Stack", "Array", "Tree"]
    )

    q3 = st.radio(
        "3. Which language is mainly used for styling web pages?",
        ["Python", "C++", "CSS", "SQL"]
    )

    if st.button("✅ Submit Quiz", use_container_width=True):

        score = 0

        if q1 == "def":
            score += 1

        if q2 == "Stack":
            score += 1

        if q3 == "CSS":
            score += 1

        st.success(
            f"🎉 Your Score: {score}/3"
        )

# ---------------- AI ASSISTANT ----------------
elif menu == "🤖 AI Study Assistant":

    st.header("🤖 AI Study Assistant")

    st.write(
        "Ask EduGenie any question related to your studies."
    )

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        st.error(
            "Gemini API key is missing. "
            "Please add it to the .env file."
        )
        st.stop()

    client = genai.Client(api_key=api_key)

    question = st.text_area(
        "💬 Your Question",
        placeholder="Example: Explain Python loops in simple words."
    )

    if st.button(
        "🚀 Ask EduGenie",
        use_container_width=True
    ):

        if question.strip():

            try:

                with st.spinner(
                    "EduGenie is thinking..."
                ):

                    response = client.models.generate_content(
                        model="gemini-3.8-flash",
                        contents=f"""
You are EduGenie, a helpful learning assistant
for BCA college students.

Explain concepts clearly and simply.
Use examples when useful.

Student question:
{question}
"""
                    )

                st.markdown("### 📚 EduGenie Answer")
                st.write(response.text)

            except Exception:

                st.warning(
                    "⚠️ Gemini is temporarily unavailable. "
                    "Please try again later."
                )

        else:

            st.warning(
                "Please enter a question."
            )

# ---------------- PROGRESS ----------------
elif menu == "📊 Progress":

    st.header("📊 Learning Progress")

    st.write(
        "Track your learning activities."
    )

    st.progress(70)

    st.write("📚 Overall Progress: 70%")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "📖 Topics Completed",
            "8"
        )

    with col2:
        st.metric(
            "📝 Quizzes Completed",
            "4"
        )

    with col3:
        st.metric(
            "🏆 Quiz Score",
            "85%"
        )

    st.success(
        "🎯 Keep learning and improve your score!"
    )