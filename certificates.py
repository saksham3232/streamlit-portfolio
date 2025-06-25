import streamlit as st
import json
from streamlit_lottie import st_lottie
import os

# Load Lottie JSON animation
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Streamlit page configuration
st.set_page_config(
    page_title="Certifications", 
    page_icon="🎓", 
    layout="wide", 
)

# Header section
st.markdown("""
    <h1 style='text-align: center; font-size: 48px;'>🎓 My Certifications</h1>
    <hr style='border: 2px solid #ddd;'>
""", unsafe_allow_html=True)

# Load Lottie animation
animation = load_lottiefile("animations/document-certificate.json")

# Content layout
col1, col2 = st.columns([2, 1])

# Certification titles and image paths
certifications = [
    {"title": "🎓 **National Coding League - Season 2** - Scaler", "file": "certificates/scaler.png"},
    {"title": "🎓 **Software Engineer Role Test Passed** - HackerRank", "file": "certificates/software_engineer_role.png"},
    {"title": "🎓 **Software Engineer Intern Role Test Passed** - HackerRank", "file": "certificates/software_engineer_intern.png"},
    {"title": "🎓 **Data Analytics & Visualization Job Simulation** - Accenture (Forage)", "file": "certificates/data_analytics_accenture.png"},
    {"title": "🎓 **Data Science Job Simulation** - BCG (Forage)", "file": "certificates/data_science_bcg.png"},
    {"title": "🎓 **Data Science Job Simulation** - British Airways (Forage)", "file": "certificates/data_science_british_airway.png"},
    {"title": "🎓 **Python (Basic)** - HackerRank", "file": "certificates/python_basic.png"},
    {"title": "🎓 **CSS (Basic)** - HackerRank", "file": "certificates/css_basic.png"},
    {"title": "🎓 **Problem Solving (Basic)** - HackerRank", "file": "certificates/problem_solving_basic.png"},
    {"title": "🎓 **Problem Solving (Intermediate)** - HackerRank", "file": "certificates/problem_solving_intermediate.png"},
    {"title": "🎓 **SQL (Basic)** - HackerRank", "file": "certificates/sql_basic.png"},
    {"title": "🎓 **SQL (Intermediate)** - HackerRank", "file": "certificates/sql_intermediate.png"},
    {"title": "🎓 **JavaScript (Basic)** - HackerRank", "file": "certificates/js_basic.png"},
    {"title": "🎓 **JavaScript (Intermediate)** - HackerRank", "file": "certificates/js_intermediate.png"},
    {"title": "🎓 **Java (Basic)** - HackerRank", "file": "certificates/java_basic.png"},
    {"title": "🎓 **Data Structures and Algorithms** - Udemy", "file": "certificates/dsa_udemy.png"},
    {"title": "🎓 **Python Project Bootcamp** - LetsUpgrade", "file": "certificates/python_bootcamp.png"},
    {"title": "🎓 **Java Project Bootcamp** - LetsUpgrade", "file": "certificates/java_bootcamp.png"},
    {"title": "🎓 **Git & GitHub Bootcamp** - LetsUpgrade", "file": "certificates/git_github.png"},
    {"title": "🎓 **Data Science with Python** - LetsUpgrade", "file": "certificates/data_science_python.png"},
    {"title": "🎓 **C++ Bootcamp** - LetsUpgrade", "file": "certificates/cpp.png"},
    {"title": "🎓 **DSA with C++ Bootcamp** - LetsUpgrade", "file": "certificates/cpp_dsa.png"},
    {"title": "🎓 **Chat GPT Bootcamp** - LetsUpgrade", "file": "certificates/chatgpt.png"},
    {"title": "🎓 **HTML CSS Bootcamp** - LetsUpgrade", "file": "certificates/html_css.png"},
    {"title": "🎓 **JavaScript Bootcamp** - LetsUpgrade", "file": "certificates/javascript.png"},
    {"title": "🎓 **Postman API Fundamentals** - LetsUpgrade", "file": "certificates/postman.png"},
]

# Left column: certifications with images
with col1:
    for cert in certifications:
        with st.expander(cert["title"]):
            st.success(cert["title"])  # Success header inside the expander
            if os.path.exists(cert["file"]):
                st.image(cert["file"], use_container_width=True)
            else:
                st.warning(f"⚠️ Could not find {cert['file']}")


    st.markdown("""
        These certifications highlight my consistent learning path in **Data Science**, **Programming**, and **Problem Solving**.
        They also reflect my ability to apply concepts in real-world simulations and competitive environments. 📈
    """)

# Right column: Lottie animation
with col2:
    if animation:
        st_lottie(animation, speed=1, height=300, key="certifications")
    else:
        st.error("⚠️ Failed to load Lottie animation.")

# Footer style
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

# Footer HTML
st.markdown(
    '<div class="footer"><b>Made with ❤️ by Saksham | © 2025</b></div>',
    unsafe_allow_html=True
)