# Streamlit Portfolio

A feature-rich, interactive personal portfolio and project showcase built with [Streamlit](https://streamlit.io/) and modern Python data science libraries.

## Table of Contents

- [Demo](#demo)
- [Features](#features)
- [Screenshots](#screenshots)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)
- [Technologies Used](#technologies-used)
- [Contact](#contact)
- [License](#license)

---

## Features

- **Dynamic Homepage:** Clean introduction, profile image, and personal summary.
- **Skills Section:** Interactive expandable lists categorized by programming languages, data science, ML, DSA, tools, databases, and soft skills.
- **Projects Showcase:** Visually-rich project cards with animation, detailed descriptions, technology stacks, and direct GitHub links. Example projects include:
    - Uber Trips Data Analysis
    - Credit Card Fraud Detection
    - IPL Score Prediction (Deep Learning)
    - IMDB Movie Review Sentiment Analysis
    - Real-time Chatbot using Groq LLM API
- **Certificates Gallery:** Visual display of achievements and certifications.
- **Achievements Timeline:** Summarizes major milestones (e.g., solving 500+ DSA problems, internships, competitions).
- **Contact Form:** Users can securely message you via a built-in form, with animated feedback and email notification integration.
- **Responsive Design:** Wide layout, custom icons, and Lottie animations for a modern look.
- **Modular Architecture:** Each section is implemented as a separate, easily extensible script.

---

## Project Structure

```
streamlit-portfolio/
│
├── app.py                # Main navigation and routing
├── Intro.py              # Homepage and introduction
├── Skills.py             # Skills & technologies
├── Projects.py           # Project gallery with details and links
├── certificates.py       # Certifications display
├── Achievements.py       # Achievements timeline
├── LetsConnect.py        # Contact form (FormSubmit & animation)
├── thank_you.py          # Thank you/confirmation page
├── requirements.txt      # Python dependencies
├── images/               # Profile, certificate, and demo images
├── animations/           # Lottie JSON files for UI animation
└── README.md             # (This file)
```

---

## Installation

### Prerequisites

- Python 3.7+
- [pip](https://pip.pypa.io/en/stable/)
- (Recommended) Create a virtual environment

### Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/saksham3232/streamlit-portfolio.git
   cd streamlit-portfolio
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app:**
   ```bash
   streamlit run app.py
   ```

---

## Usage

- The homepage introduces you with a photo, summary, and current focus.
- Navigate using the sidebar to view:
    - **Skills:** Explore technical and soft skills grouped by category.
    - **Projects:** Browse projects, read details, and visit project GitHub repos.
    - **Achievements:** See DSA milestones, internships, and hackathons.
    - **Certificates:** Visual gallery of your earned certifications.
    - **Contact:** Securely send a message via the contact form.
- Animations and responsive layouts enhance user experience.

---

## Customization

- **Personal Info:** Edit `Intro.py` for your name, bio, and education.
- **Skills:** Update the `skills` dictionary in `Skills.py` to match your expertise.
- **Projects:** Add or edit project sections in `Projects.py` (description, tech stack, links, animations).
- **Achievements & Certifications:** Update the lists in `Achievements.py` and `certificates.py`.
- **Contact Integration:** The contact form uses FormSubmit (or similar API) for messaging; update endpoints as needed.
- **Images/Animations:** Replace images in `images/` and animations in `animations/` as desired. Supported by [LottieFiles](https://lottiefiles.com/).

---

## Technologies Used

- **Frontend:** Streamlit, HTML/CSS, Lottie Animations
- **Backend/Data:** Python (pandas, numpy, scikit-learn, tensorflow, keras, flask, nltk, xgboost, matplotlib, seaborn)
- **Deployment:** Localhost, Streamlit Cloud, or any Python hosting service
- **Other:** FormSubmit/email integration for contact, PIL for image processing

---

## Contact

For questions, collaboration, or feedback:

- **Email:** your.email@example.com
- **LinkedIn:** [your-linkedin](https://linkedin.com/in/your-profile)
- **GitHub:** [saksham3232](https://github.com/saksham3232)

---

*Built with ❤️ by Saksham Maurya. Powered by Streamlit and Python.*
