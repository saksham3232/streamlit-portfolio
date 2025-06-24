import streamlit as st
import json 
from streamlit_lottie import st_lottie

# Load local lottie animation
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# --- Page Configuration ---
st.set_page_config(
    page_title="Saksham's Portfolio",
    page_icon=":wave:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Intro Section ---
st.markdown("""
    ## Hi, I'm Saksham 👋
    # A Data Science Student 🚀  

    By day, I'm diving deep into **Data Structures and Algorithms (DSA)** to sharpen my problem-solving mindset. By night, I immerse myself in **Data Science**, working with real-world datasets to build models in **Machine Learning**, **Deep Learning**, and **Natural Language Processing (NLP)**.  

    Currently pursuing my Bachelor's in Computer Applications (BCA), I focus on bridging theory with practice through impactful projects. I specialize in tools and frameworks like **Python**, **C++**, **SQL**, **Streamlit**, **Flask**, **pandas**, **NumPy**, **matplotlib**, **Seaborn**, **Scikit-learn**, **TensorFlow**, and **Keras**.

    🧠 My interest lies in making data-driven decisions and turning raw data into actionable insights. Whether it’s **fraud detection**, **sentiment analysis**, or **score prediction**, I love creating models that **solve real problems**.

    ⚙️ My journey includes:
    - Building intuitive data apps using **Streamlit**
    - Developing and deploying ML models using **Scikit-learn**, **XGBoost**, and **TensorFlow**
    - Working with **large datasets** and applying **EDA**, **feature engineering**, and **model evaluation**
    - Exploring **LLMs**, AI trends, and **ethical AI** practices

    💼 I’ve successfully completed **job simulations with Accenture and BCG**, along with solving over **500+ DSA problems** on platforms like LeetCode and GFG using **Striver's A2Z DSA Sheet**.

    📂 This portfolio showcases my **projects**, **achievements**, and **certifications** — reflecting my growth and dedication in the field of AI and Data Science.

    🌟 When I'm not coding, you'll find me exploring the latest tech trends, contributing to open-source, or writing blogs on machine learning concepts. I believe in continuous learning and strive to stay at the edge of innovation.

    📫 Let's connect on [LinkedIn](https://www.linkedin.com/in/saksham-maurya-3feb) | [GitHub](https://github.com/saksham3232) | [Email](mailto:sakshammaurya3232@gmail.com)  

    🤝 I'm open to **internships**, **research roles**, and **collaborations** in the field of **AI**, **ML**, or **Data Science**. If you have an idea — let’s build it together!
""")

# --- Resume Download ---
st.write("📄 Here's my resume:")
with open("CV_Saksham.pdf", "rb") as file:
    btn = st.download_button(
        label="Download Resume",
        data=file,
        file_name="Saksham_Maurya_Resume.pdf",
        mime="application/pdf"
    )

# --- Lottie Animation ---

# Load Lottie Animation
animation = load_lottiefile("animations/intro.json")
if animation:
    st_lottie(animation, speed=1, height=300, key="home")
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