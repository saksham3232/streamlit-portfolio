import streamlit as st
import json
from streamlit_lottie import st_lottie

# Load local lottie animation
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Page Configuration
st.set_page_config(page_title="My Projects", page_icon="💼", layout="wide")

# Title
# Title and Header
st.markdown("""
    <h1 style='text-align: center; font-size: 48px;'>My Projects 💼</h1>
    <hr style='border: 2px solid #ddd;'>
""", unsafe_allow_html=True)

# Project 1: Uber Trips Data Analysis
with st.container():
    img_col, text_col = st.columns((1, 2))
    with img_col:
        animation = load_lottiefile("animations/business-analysis.json")
        if animation:
            st_lottie(animation, speed=1, height=300, key="uber")
    with text_col:
        st.write("### 🚕 Uber Trips Data Analysis")
        st.write("""
        - Cleaned and preprocessed Uber trip data, handled missing values, and categorized trips.
        - Performed exploratory data analysis to visualize ride patterns and mileage distributions.
        - Identified correlations between trip categories, time of day, and ride behaviors.
        """)
        with st.expander("🔧 Technologies Used"):
            st.write("- Python, Pandas, NumPy, Matplotlib, Seaborn")
        with st.expander("📂 Project Link"):
            st.write("[View on GitHub](https://github.com/saksham3232/Uber-Trips-Analysis)")

# Project 2: Credit Card Fraud Detection
with st.container():
    st.write("---")
    img_col, text_col = st.columns((1, 2))
    with img_col:
        animation = load_lottiefile("animations/file-searching.json")
        if animation:
            st_lottie(animation, speed=1, height=300, key="fraud")
    with text_col:
        st.write("### 💳 Credit Card Fraud Detection")
        st.write("""
        - Analyzed and preprocessed transaction data to identify fraudulent activity.
        - Trained Random Forest classifier with 97% precision.
        - Evaluated model with F1-score, confusion matrix, and MCC.
        """)
        with st.expander("🔧 Technologies Used"):
            st.write("- Python, Scikit-Learn, Pandas, Matplotlib, Seaborn")
        with st.expander("📂 Project Link"):
            st.write("[View on GitHub](https://github.com/saksham3232/Credit-Card-Fraud-Detection)")

# Project 3: IPL Score Prediction
with st.container():
    st.write("---")
    img_col, text_col = st.columns((1, 2))
    with img_col:
        animation = load_lottiefile("animations/gear-loader.json")
        if animation:
            st_lottie(animation, speed=1, height=300, key="ipl")
    with text_col:
        st.write("### 🏏 IPL Score Prediction")
        st.write("""
        - Preprocessed IPL data with label encoding and feature scaling.
        - Built a deep learning model using TensorFlow and Keras.
        - Deployed an interactive tool for real-time IPL score predictions.
        """)
        with st.expander("🔧 Technologies Used"):
            st.write("- Python, TensorFlow, Keras, Streamlit")
        with st.expander("📂 Project Link"):
            st.write("[View on GitHub](https://github.com/saksham3232/IPL-Score-Prediction)")

# Project 4: IMDB Movie Review Sentiment Analysis
with st.container():
    st.write("---")
    img_col, text_col = st.columns((1, 2))
    with img_col:
        animation = load_lottiefile("animations/customer-service-chat.json")
        if animation:
            st_lottie(animation, speed=1, height=300, key="imdb")
    with text_col:
        st.write("### 🎬 IMDB Movie Review Sentiment Analysis")
        st.write("""
        - Built NLP pipeline using TF-IDF and Logistic Regression.
        - Achieved over 90% accuracy in classifying positive/negative reviews.
        - Visualized key sentiment indicators using word clouds and bar plots.
        """)
        with st.expander("🔧 Technologies Used"):
            st.write("- Python, NLTK, Scikit-learn, Seaborn, Matplotlib")
        with st.expander("📂 Project Link"):
            st.write("[View on GitHub](https://github.com/saksham3232/IMDB-Sentiment-Analysis)")

# Project 5: Chatbot using Groq API
with st.container():
    st.write("---")
    img_col, text_col = st.columns((1, 2))
    with img_col:
        animation = load_lottiefile("animations/astronaut-with-space-shuttle.json")
        if animation:
            st_lottie(animation, speed=1, height=300, key="chatbot")
    with text_col:
        st.write("### 🤖 Chatbot using Groq API")
        st.write("""
        - Integrated Groq LLM API to create a responsive, intelligent chatbot.
        - Added conversational memory and context awareness.
        - Packaged as a web app with Streamlit for real-time use.
        """)
        with st.expander("🔧 Technologies Used"):
            st.write("- Python, Groq API, Streamlit, LangChain")
        with st.expander("📂 Project Link"):
            st.write("[View on GitHub](https://github.com/saksham3232/Groq-Chatbot)")

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