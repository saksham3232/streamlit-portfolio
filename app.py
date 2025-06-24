import streamlit as st


intro_page = st.Page("Intro.py", title = "Home", icon = ":material/home:")
skills_page = st.Page("Skills.py", title = "My Skills", icon = ":material/palette:")
project_page = st.Page("Projects.py", title = "My Projects", icon = ":material/work:")
certificates_page = st.Page("certificates.py", title = "My Certificates", icon = ":material/emoji_events:")
ach_page = st.Page("Achievements.py", title = "See My Achievements", icon = ":material/sports_score:")
conn_page = st.Page("LetsConnect.py", title = "Let's Connect", icon = ":material/hub:")

pg = st.navigation(
    {
        "Navigate Here" : [intro_page, skills_page, project_page, certificates_page, ach_page, conn_page]
    })

pg.run()