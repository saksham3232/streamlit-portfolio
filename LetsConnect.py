import streamlit as st
import json
from streamlit_lottie import st_lottie


# Load local lottie animation
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
    
# --- Page Configuration ---
st.set_page_config(
    page_title="Contact Me",
    page_icon="📞",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load a Lottie animation for the contact page
lottie_contact = load_lottiefile("animations/connect.json")

# Custom CSS only for the submit button (contact-form container block removed)
st.markdown(
    """
    <style>
    .custom-button {
      background-color: #4CAF50;
      color: white;
      border: none;
      padding: 10px 20px;
      border-radius: 5px;
      cursor: pointer;
      font-size: 16px;
    }
    .custom-button:hover {
      background-color: #45a049;
    }
    </style>
    """, unsafe_allow_html=True)

# Page title and introduction
st.title("Contact Me")
st.write("Fill out the form below to get in touch.")

# Divide the page into two columns for balanced layout
col1, col2 = st.columns([0.6, 0.4])

with col1:
    # Create a contact form using Streamlit's form component without extra HTML block
    with st.form(key='contact_form'):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submit_button = st.form_submit_button("Send Message")
        
        if submit_button:
            st.success("Thank you for your message! We will get back to you soon.")

with col2:
    if lottie_contact:
        st_lottie(lottie_contact, height=300, key="contact")
    else:
        st.write("Animation could not be loaded.")


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