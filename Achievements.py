import streamlit as st
import json 
from streamlit_lottie import st_lottie

# Load local lottie animation
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
# Page Configuration
st.set_page_config(page_title="My Achievements", page_icon="🏆", layout="wide")

# Title and Header
st.markdown("""
    <h1 style='text-align: center; font-size: 48px;'>🏆 My Achievements</h1>
    <hr style='border: 2px solid #ddd;'>
""", unsafe_allow_html=True)

# Load Lottie Animation
lottie_animation = load_lottiefile("animations/achievements.json")

# Columns for Layout
col1, col2 = st.columns([2, 1])

# Achievements Section
with col1:
    achievements = [
        "✅ Solved **500+ DSA problems** across LeetCode & GeeksforGeeks using the **Striver A2Z DSA Sheet**.",
        "🏅 Passed **Software Engineer** & **Software Engineer Intern** role test at HackerRank.",
        "🚀 Semi-Finalist in **Scaler National Coding League - Season 2**.",
        "🎓 Successfully completed **Python Project Bootcamp** and **Java Bootcamp** with LetsUpgrade.",
        "🏅 Certified in **Java (Basic)**, **Problem Solving (Basic & Intermediate)** by HackerRank.",
        "📜 Completed **Data Science job simulations** by **British Airways** and **BCG-X** on Forage.",
        "💡 Built impactful ML projects like **Uber Data Analysis**, **Credit Card Fraud Detection**, and **IPL Score Predictor**."
    ]

    for achievement in achievements:
        st.success(achievement)

    st.markdown("""
        **Every milestone, from cracking problems to completing projects, reflects my commitment to continuous learning.**  
        I'm grateful for each opportunity and excited about what lies ahead. 🚀
    """)

# Animation Column
with col2:
    if lottie_animation:
        st_lottie(lottie_animation, speed=1, height=300, key="achievements")
    else:
        st.error("⚠️ Failed to load Lottie animation.")

# Topics of Interest
st.write("---")
st.markdown("""
    <h2 style='text-align: center;'>📚 I Like To Talk About</h2>
""", unsafe_allow_html=True)

topics = [
    "📊 Data Science", "🤖 Machine Learning", "🧠 Deep Learning", "🚀 Artificial Intelligence",
    "🖼️ Computer Vision", "📜 Natural Language Processing", "📌 Data Structures & Algorithms", "💡 Self-Improvement"
]

cols = st.columns(2)
for i, topic in enumerate(topics):
    with cols[i % 2]:
        st.info(topic)

#--- Footer Styling ---
st.markdown("""
<style>
@keyframes fadeIn {
    from {opacity: 0;}
    to {opacity: 1;}
}
.footer {
    animation: fadeIn 2s ease-in;
    text-align: center;
    font-size: 18px;
    margin-top: 20px;
    color: #555;
}
</style>
""", unsafe_allow_html=True)

# --- Footer HTML ---
st.markdown(
    '<div class="footer"><b>Made with ❤️ by Saksham | © 2025</b></div>',
    unsafe_allow_html=True
)