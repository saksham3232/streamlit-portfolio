# Saksham's Portfolio - HTML Version

This repository contains a complete HTML/CSS/JavaScript conversion of the original Streamlit portfolio application.

## 🌟 Features

- **Multi-page Navigation**: Smooth navigation between different sections
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **Interactive Elements**: 
  - Expandable sections (similar to Streamlit st.expander)
  - Contact form with FormSubmit integration
  - Resume download functionality
- **Lottie Animations**: Beautiful animations throughout the site
- **Same-to-Same Conversion**: Maintains exact visual appearance and functionality of the original Streamlit app

## 📁 File Structure

```
├── index.html          # Main HTML file with all pages
├── styles.css          # Complete styling to match Streamlit appearance
├── script.js           # JavaScript for interactivity and navigation
├── animations/         # Lottie JSON animation files
├── images/            # Profile and other images
├── certificates/      # Certificate images
├── CV_Saksham.pdf    # Resume file
└── README.md         # This file
```

## 🚀 How to Run

### Option 1: Simple HTTP Server (Recommended)
```bash
# Using Python
python -m http.server 8000

# Using Node.js (if you have it)
npx serve .

# Using PHP (if you have it)
php -S localhost:8000
```

Then open your browser and go to `http://localhost:8000`

### Option 2: Direct File Access
Simply open `index.html` in your web browser by double-clicking it.

**Note**: Some features like Lottie animations may not work properly when opening directly due to browser security restrictions. Using a local server is recommended.

## 📱 Pages Included

1. **Home** - Personal introduction, profile, resume download
2. **My Skills** - Technical and soft skills organized by categories
3. **My Projects** - Detailed project showcases with GitHub links
4. **My Certificates** - Professional certifications with images
5. **See My Achievements** - Accomplishments and topics of interest
6. **Let's Connect** - Contact form for getting in touch

## 🛠️ Technologies Used

- **HTML5**: Semantic markup structure
- **CSS3**: Modern styling with animations and responsive design
- **JavaScript (ES6+)**: Interactive functionality and form handling
- **Lottie Web**: Beautiful animations
- **Font Awesome**: Icon library
- **FormSubmit**: Contact form backend service

## ✨ Key Conversions from Streamlit

| Streamlit Feature | HTML Equivalent |
|-------------------|----------------|
| `st.navigation()` | JavaScript page switching |
| `st.expander()` | CSS/JS collapsible sections |
| `st.columns()` | CSS Grid layouts |
| `st_lottie()` | Lottie-player web component |
| `st.form()` | HTML form with JS submission |
| `st.download_button()` | Direct download link |
| `st.markdown()` | HTML elements with CSS styling |

## 🎨 Styling

The CSS maintains the exact visual appearance of the original Streamlit app, including:
- Color scheme and typography
- Spacing and layout
- Animations and transitions
- Responsive behavior
- Button styles and hover effects

## 📧 Contact Form

The contact form uses FormSubmit.co service to handle form submissions without requiring a backend server. Messages are sent directly to the configured email address.

## 🌐 Browser Compatibility

- ✅ Chrome (recommended)
- ✅ Firefox
- ✅ Safari
- ✅ Edge
- ✅ Mobile browsers

## 📝 Customization

To customize this portfolio for your own use:

1. Update personal information in `index.html`
2. Replace images in `images/` and `certificates/` folders
3. Update the resume file `CV_Saksham.pdf`
4. Modify colors and styling in `styles.css`
5. Update contact form email in `script.js`

## 🚀 Deployment

This static site can be easily deployed on:
- GitHub Pages
- Netlify
- Vercel
- Any static hosting service

Simply upload all files to your hosting service, and the site will be live!

## 📞 Contact

**Saksham Maurya**
- Email: sakshammaurya3232@gmail.com
- LinkedIn: [saksham-maurya-3feb](https://www.linkedin.com/in/saksham-maurya-3feb)
- GitHub: [saksham3232](https://github.com/saksham3232)

---

Made with ❤️ by Saksham | © 2025