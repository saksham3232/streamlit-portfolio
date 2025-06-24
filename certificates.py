import streamlit as st
import json
from streamlit_lottie import st_lottie

# Load local lottie animation
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Page Configuration
st.set_page_config(page_title="Certifications", page_icon="🎓", layout="wide")

# Title and Header
st.markdown("""
    <h1 style='text-align: center; font-size: 48px;'>🎓 My Certifications</h1>
    <hr style='border: 2px solid #ddd;'>
""", unsafe_allow_html=True)

# Load Lottie Animation
animation = load_lottiefile("animations/document-certificate.json")

# Content Layout
col1, col2 = st.columns([2, 1])

# Certifications Section
with col1:
    certifications = [
        "🎓 **Software Engineer Role Test Passed** - HackerRank",
        "🎓 **Software Engineer Intern Role Test Passed** - HackerRank",
        "🎓 **Data Analytics & Visualization Job Simulation** - Accenture (Forage)",
        "🎓 **Data Science Job Simulation** - BCG (Forage)", 
        "🎓 **Python (Basic)** - HackerRank",
        "🎓 **CSS (Basic)** - HackerRank",
        "🎓 **Problem Solving (Basic)** - HackerRank",
        "🎓 **Problem Solving (Intermediate)** - HackerRank",
        "🎓 **SQL (Basic)** - HackerRank",
        "🎓 **SQL (Intermediate)** - HackerRank",
        "🎓 **JavaScript (Basic)** - HackerRank",
        "🎓 **JavaScript (Intermediate)** - HackerRank",
        "🎓 **Java (Basic)** - HackerRank",
        "🎓 **Data Structures and Algorithms** - Udemy",
        "🎓 **Python Project Bootcamp** - LetsUpgrade",
        "🎓 **Java Bootcamp** - LetsUpgrade",
    ]

    for cert in certifications:
        st.success(cert)

    st.markdown("""
        These certifications highlight my consistent learning path in **Data Science**, **Programming**, and **Problem Solving**.
        They also reflect my ability to apply concepts in real-world simulations and competitive environments. 📈
    """)

# Lottie Animation
with col2:
    if animation:
        st_lottie(animation, speed=1, height=200, key="certifications")
    else:
        st.error("⚠️ Failed to load Lottie animation.")


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