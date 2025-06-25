import streamlit as st
import json 
from streamlit_lottie import st_lottie

# Load local lottie animation
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# --- Page Configuration ---
st.set_page_config(page_title="My Skills", page_icon="🚀", layout="wide", initial_sidebar_state='auto')

# Title and Header
st.markdown("""
    <h1 style='text-align: center; font-size: 48px;'>My Skills 🚀</h1>
    <hr style='border: 2px solid #ddd;'>
""", unsafe_allow_html=True)

# --- Load Lottie Animation ---
lottie_animation = load_lottiefile("animations/skills.json")

# --- Layout Columns ---
col1, col2 = st.columns([2, 1])

# --- Skills Section ---
with col1:
    skills = {
        "🖥️ Programming Languages": [
            "C", "C++", "Java", "Python", "SQL", "HTML", "CSS", "JavaScript"
        ],
        "📚 Libraries & Frameworks": [
            "NumPy", "Pandas", "Matplotlib", "Seaborn", "Scikit-learn", 
            "Streamlit", "Flask", "TensorFlow", "Keras", "NLTK"
        ],
        "📊 Data Science & Analytics": [
            "Exploratory Data Analysis (EDA)", "Feature Engineering",
            "Data Preprocessing", "Model Evaluation", "MLflow"
        ],
        "🧠 Machine Learning & Deep Learning": [
            "Supervised & Unsupervised Learning", "XGBoost", "Neural Networks", 
            "Deep Learning", "Natural Language Processing (NLP)", 
            "Computer Vision", "Transformers"
        ],
        "🧮 DSA & Problem Solving": [
            "Striver A2Z DSA Sheet", "LeetCode", "GeeksforGeeks", 
            "Algorithmic Thinking", "Optimization Techniques"
        ],
        "🛠️ Tools & Platforms": [
            "Git", "GitHub", "VS Code", "Jupyter Notebook", "Google Colab", 
            "Anaconda", "Docker"
        ],
        "🗄️ Databases": [
            "SQL", "SQLite"
        ],
        "💡 Soft Skills": [
            "Adaptability", "Continuous Learning", "Problem Solving", 
            "Time Management", "Discipline", "Communication", 
            "Teamwork", "Creativity & Innovation"
        ]
    }

    for category, items in skills.items():
        with st.expander(category):
            st.success(", ".join(items))


# --- Lottie Animation Column ---
with col2:
    if lottie_animation:
        st_lottie(lottie_animation, speed=1, height=300, key="skills")
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

# --- JavaScript to Auto-Collapse Sidebar on Mobile ---
st.markdown("""
    <script>
    const mediaQuery = window.matchMedia('(max-width: 768px)');
    if (mediaQuery.matches) {
        const sidebar = parent.document.querySelector('.css-1lcbmhc.e1fqkh3o3');
        if (sidebar && sidebar.style.display !== 'none') {
            const toggleButton = parent.document.querySelector('[data-testid="collapsedControl"]');
            if (toggleButton) toggleButton.click();
        }
    }
    </script>
""", unsafe_allow_html=True)