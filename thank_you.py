import streamlit as st
import time
from streamlit_lottie import st_lottie
import json

# Load Lottie animation
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Page config
st.set_page_config(
    page_title="Thank You",
    page_icon="✅",
    layout="centered",
    initial_sidebar_state="auto"
)

# Load animation
lottie_thank_you = load_lottiefile("animations/thank_you.json")

# Display
st.title("🎉 Thank You!")
st.subheader("Your message has been sent successfully.")
st.write("I appreciate you reaching out. I’ll get back to you soon!")

if lottie_thank_you:
    st_lottie(lottie_thank_you, height=300)
else:
    st.info("✅ Submission received.")

# Footer
st.markdown(
    "<hr><div style='text-align: center; color: gray;'>Made with ❤️ by Saksham | © 2025</div>",
    unsafe_allow_html=True
)