import streamlit as st
import json
import smtplib
from email.message import EmailMessage
from streamlit_lottie import st_lottie

# --- Load Lottie Animation ---
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# --- Streamlit Page Config ---
st.set_page_config(
    page_title="Contact Me",
    page_icon="📞",
    layout="wide",
    initial_sidebar_state="auto"
)

# --- Load Contact Animation ---
lottie_contact = load_lottiefile("animations/gmail.json")

# --- Custom Button Styling ---
st.markdown("""
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

# --- SMTP Email Sending Function ---
def submit_to_smtp(name, email, message):
    # Define sender email credentials
    sender_email = "sakshammaurya678@gmail.com"
    sender_password = "anozxvbkqsjrzyqv"  # Use app password, NOT your Gmail password

    # Compose email
    msg = EmailMessage()
    msg['Subject'] = "New Contact Form Submission"
    msg['From'] = sender_email
    msg['To'] = sender_email  # Send to yourself
    msg.set_content(f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}")

    # Send via Gmail SMTP server
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, sender_password)
            smtp.send_message(msg)
        return True
    except Exception as e:
        print(f"Email sending failed: {e}")
        return False

# --- Page Title ---
st.title("Contact Me")
st.write("Fill out the form below to get in touch.")

# --- Layout Columns ---
col1, col2 = st.columns([0.6, 0.4])

with col1:
    with st.form(key='contact_form'):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submit_button = st.form_submit_button("Send Message")

        if submit_button:
            if name and email and message:
                success = submit_to_smtp(name, email, message)
                if success:
                    st.success("✅ Message sent successfully!")
                else:
                    st.error("❌ Failed to send message. Please try again.")
            else:
                st.warning("⚠️ Please fill out all fields.")

with col2:
    if lottie_contact:
        st_lottie(lottie_contact, height=300, key="contact")
    else:
        st.write("⚠️ Animation could not be loaded.")

# --- Footer Styling ---
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
