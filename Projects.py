import streamlit as st
import json
from streamlit_lottie import st_lottie

# Load local lottie animation
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Page Configuration
st.set_page_config(
    page_title="My Projects", 
    page_icon="💼",
    layout="wide"
)

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
            - Cleaned and standardized Uber trip data, addressed missing values, and unified ride categories for accurate analysis.
            - Explored trends in ride frequency, fare efficiency, and cancellation rates using visualizations and statistical metrics.
            - Revealed UberX as the dominant ride type, measured the impact of COVID-19 on trip volume, and provided actionable recommendations to optimize services and pricing strategies.
        """)
        with st.expander("🔧 Technologies Used"):
            st.success("- Python, Pandas, NumPy, Matplotlib, Seaborn")
        with st.expander("📂 Project Link"):
            st.success("- [View on GitHub](https://github.com/saksham3232/Uber-Trips-Data-Analysis)")

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
        - Cleaned and analyzed highly imbalanced credit card transaction data; performed EDA, statistical analysis, and correlation heatmaps to extract fraud patterns.
        - Engineered a robust fraud detection pipeline using SMOTE for class balancing and trained a Random Forest classifier with class weighting; achieved 87% precision and 83% recall on unseen data.
        - Evaluated model performance using F1-score (0.85), Matthews Correlation Coefficient (0.85), and confusion matrix to ensure reliability on minority class prediction.
        """)
        with st.expander("🔧 Technologies Used"):
            st.success("- Python, Scikit-Learn, Pandas, Matplotlib, Seaborn, SMOTE, Flask")
        with st.expander("📂 Project Link"):
            st.success("- [View on GitHub](https://github.com/saksham3232/Credit-Card-Fraud-Detection)")

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
        - Preprocessed IPL match data (2008–2017) using label encoding, train-test split, and Min-Max feature scaling for neural network input.
        - Developed and trained a Keras/TensorFlow deep learning regression model to predict total match scores, evaluated using MAE, MSE, RMSE, and R² metrics.
        - Built both an interactive ipywidgets UI for Jupyter and a Flask web app for real-time score prediction, with model and encoders saved for deployment.
        """)
        with st.expander("🔧 Technologies Used"):
            st.success("- Python, TensorFlow, Keras, Flask, Pandas, Scikit-learn")
        with st.expander("📂 Project Link"):
            st.success("- [View on GitHub](https://github.com/saksham3232/IPL-Score-Predictor)")

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
            - Developed an end-to-end sentiment analysis application using Simple RNN with TensorFlow/Keras on the IMDB movie review dataset.
            - Attained over 93% training accuracy and more than 84% validation accuracy, leveraging early stopping to prevent overfitting.
            - Implemented complete data preprocessing, review decoding for interpretability, and exported the trained model for deployment via Streamlit.
        """)
        with st.expander("🔧 Technologies Used"):
            st.success("- Python, NLTK, Scikit-learn, TensorFlow, Keras, Streamlit")
        with st.expander("📂 Project Link"):
            st.success("- [View on GitHub](https://github.com/saksham3232/IMDB-Movie-Review-Sentiment-Analysis)")

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
        - Integrated Groq LLM API for seamless real-time chatbot interaction, leveraging both `.env` and Streamlit secrets management for secure API access.
        - Engineered session-based logic to maintain chat history and context, enabling accurate and contextually aware responses throughout the conversation.
        - Developed and deployed a user-friendly web application interface using Streamlit, providing an interactive and responsive chat experience.
        """)
        with st.expander("🔧 Technologies Used"):
            st.success("- Python, Groq API, Streamlit, dotenv, Streamlit Secrets")
        with st.expander("📂 Project Link"):
            st.success("- [View on GitHub](https://github.com/saksham3232/chat-bot)")

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