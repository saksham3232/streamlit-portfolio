// Wait for DOM to load
document.addEventListener('DOMContentLoaded', function() {
    // Initialize the page
    initializeNavigation();
    initializeExpanders();
    initializeContactForm();
    
    // Show home page by default
    showPage('home');
});

// Navigation functionality
function initializeNavigation() {
    const navItems = document.querySelectorAll('.nav-item');
    
    navItems.forEach(item => {
        item.addEventListener('click', function() {
            const page = this.getAttribute('data-page');
            
            // Remove active class from all nav items
            navItems.forEach(nav => nav.classList.remove('active'));
            
            // Add active class to clicked item
            this.classList.add('active');
            
            // Show the corresponding page
            showPage(page);
        });
    });
}

// Show specific page
function showPage(pageId) {
    // Hide all pages
    const pages = document.querySelectorAll('.page');
    pages.forEach(page => page.classList.remove('active'));
    
    // Show the selected page
    const selectedPage = document.getElementById(pageId);
    if (selectedPage) {
        selectedPage.classList.add('active');
    }
    
    // Scroll to top
    window.scrollTo(0, 0);
}

// Expander functionality (like Streamlit st.expander)
function initializeExpanders() {
    const expanders = document.querySelectorAll('.expander');
    
    expanders.forEach(expander => {
        const header = expander.querySelector('.expander-header');
        
        header.addEventListener('click', function() {
            // Toggle active class
            expander.classList.toggle('active');
            
            // Get the content
            const content = expander.querySelector('.expander-content');
            
            if (expander.classList.contains('active')) {
                content.style.display = 'block';
                // Add smooth transition
                content.style.opacity = '0';
                setTimeout(() => {
                    content.style.opacity = '1';
                }, 10);
            } else {
                content.style.display = 'none';
            }
        });
    });
}

// Contact form functionality
function initializeContactForm() {
    const form = document.getElementById('contactForm');
    const messageDiv = document.getElementById('formMessage');
    
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        // Get form data
        const formData = new FormData(form);
        const name = formData.get('name');
        const email = formData.get('email');
        const message = formData.get('message');
        
        // Validate form
        if (!name || !email || !message) {
            showFormMessage('⚠️ Please fill out all fields.', 'warning');
            return;
        }
        
        // Show loading state
        const submitBtn = form.querySelector('.submit-btn');
        const originalText = submitBtn.innerHTML;
        submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Sending...';
        submitBtn.disabled = true;
        
        // Submit to FormSubmit
        submitToFormSubmit(name, email, message)
            .then(success => {
                if (success) {
                    showFormMessage('✅ Message sent successfully!', 'success');
                    form.reset();
                } else {
                    showFormMessage('❌ Failed to send message. Please try again.', 'error');
                }
            })
            .catch(error => {
                console.error('Form submission error:', error);
                showFormMessage('❌ Failed to send message. Please try again.', 'error');
            })
            .finally(() => {
                // Reset button
                submitBtn.innerHTML = originalText;
                submitBtn.disabled = false;
            });
    });
}

// Submit form to FormSubmit service
async function submitToFormSubmit(name, email, message) {
    try {
        const formData = new FormData();
        formData.append('name', name);
        formData.append('email', email);
        formData.append('message', message);
        formData.append('_captcha', 'false');
        formData.append('_template', 'box');
        formData.append('_subject', 'New Contact Form Submission');
        
        const response = await fetch('https://formsubmit.co/sakshammaurya678@gmail.com', {
            method: 'POST',
            body: formData
        });
        
        return response.ok;
    } catch (error) {
        console.error('FormSubmit error:', error);
        return false;
    }
}

// Show form message
function showFormMessage(message, type) {
    const messageDiv = document.getElementById('formMessage');
    messageDiv.textContent = message;
    messageDiv.className = `form-message ${type}`;
    
    // Hide message after 5 seconds
    setTimeout(() => {
        messageDiv.style.display = 'none';
        messageDiv.className = 'form-message';
    }, 5000);
}

// Smooth scrolling for internal links
document.addEventListener('click', function(e) {
    if (e.target.tagName === 'A' && e.target.getAttribute('href') && e.target.getAttribute('href').startsWith('#')) {
        e.preventDefault();
        const targetId = e.target.getAttribute('href').substring(1);
        const targetElement = document.getElementById(targetId);
        if (targetElement) {
            targetElement.scrollIntoView({ behavior: 'smooth' });
        }
    }
});

// Handle image loading errors
document.addEventListener('DOMContentLoaded', function() {
    const images = document.querySelectorAll('img');
    
    images.forEach(img => {
        img.addEventListener('error', function() {
            this.style.display = 'none';
            
            // For certificate images, show a placeholder
            if (this.classList.contains('certificate-image')) {
                const placeholder = document.createElement('div');
                placeholder.className = 'image-placeholder';
                placeholder.textContent = '⚠️ Certificate image not found';
                placeholder.style.cssText = `
                    background-color: #f8f9fa;
                    border: 2px dashed #dee2e6;
                    padding: 2rem;
                    text-align: center;
                    color: #6c757d;
                    border-radius: 0.25rem;
                    margin-top: 0.5rem;
                `;
                this.parentNode.insertBefore(placeholder, this.nextSibling);
            }
            
            // For profile image, show a placeholder
            if (this.classList.contains('profile-image')) {
                const placeholder = document.createElement('div');
                placeholder.className = 'profile-placeholder';
                placeholder.textContent = '👤';
                placeholder.style.cssText = `
                    width: 200px;
                    height: 200px;
                    background-color: #f8f9fa;
                    border: 2px dashed #dee2e6;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    font-size: 4rem;
                    border-radius: 10px;
                    color: #6c757d;
                `;
                this.parentNode.insertBefore(placeholder, this.nextSibling);
            }
        });
    });
});

// Handle Lottie animation loading errors
document.addEventListener('DOMContentLoaded', function() {
    const lottieElements = document.querySelectorAll('lottie-player');
    
    lottieElements.forEach(lottie => {
        lottie.addEventListener('error', function() {
            console.warn('Lottie animation failed to load:', this.src);
            
            // Create a placeholder
            const placeholder = document.createElement('div');
            placeholder.className = 'animation-placeholder';
            placeholder.innerHTML = '🎨';
            placeholder.style.cssText = `
                width: ${this.style.width || '300px'};
                height: ${this.style.height || '300px'};
                background-color: #f8f9fa;
                border: 2px dashed #dee2e6;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 4rem;
                border-radius: 0.5rem;
                color: #6c757d;
            `;
            
            this.parentNode.insertBefore(placeholder, this.nextSibling);
            this.style.display = 'none';
        });
    });
});

// Add keyboard navigation
document.addEventListener('keydown', function(e) {
    // Navigate with arrow keys when focused on nav
    if (e.target.classList.contains('nav-item')) {
        const navItems = Array.from(document.querySelectorAll('.nav-item'));
        const currentIndex = navItems.indexOf(e.target);
        
        let nextIndex;
        
        if (e.key === 'ArrowLeft') {
            nextIndex = currentIndex > 0 ? currentIndex - 1 : navItems.length - 1;
        } else if (e.key === 'ArrowRight') {
            nextIndex = currentIndex < navItems.length - 1 ? currentIndex + 1 : 0;
        } else if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            e.target.click();
            return;
        } else {
            return;
        }
        
        e.preventDefault();
        navItems[nextIndex].focus();
    }
});

// Add focus indicators for accessibility
document.addEventListener('DOMContentLoaded', function() {
    const style = document.createElement('style');
    style.textContent = `
        .nav-item:focus,
        .expander-header:focus,
        .download-btn:focus,
        .submit-btn:focus {
            outline: 2px solid #ff4b4b;
            outline-offset: 2px;
        }
        
        .form-group input:focus,
        .form-group textarea:focus {
            outline: 2px solid #ff4b4b;
            outline-offset: 2px;
        }
    `;
    document.head.appendChild(style);
});

// Performance optimization: Lazy load animations
document.addEventListener('DOMContentLoaded', function() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '50px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const lottie = entry.target;
                if (lottie.tagName === 'LOTTIE-PLAYER' && !lottie.hasAttribute('data-loaded')) {
                    lottie.setAttribute('data-loaded', 'true');
                    // The lottie-player will handle loading automatically
                }
            }
        });
    }, observerOptions);
    
    const lottieElements = document.querySelectorAll('lottie-player');
    lottieElements.forEach(lottie => observer.observe(lottie));
});

// Add loading indicator for slow connections
window.addEventListener('load', function() {
    // Hide any loading indicators
    const loadingElements = document.querySelectorAll('.loading');
    loadingElements.forEach(el => el.style.display = 'none');
});

// Console welcome message
console.log(`
🎉 Welcome to Saksham's Portfolio!
🚀 This portfolio has been converted from Streamlit to pure HTML/CSS/JS
📧 Contact: sakshammaurya3232@gmail.com
🔗 GitHub: https://github.com/saksham3232
`);