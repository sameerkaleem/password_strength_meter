import streamlit as st
import re
import random
import string

# Common passwords to blacklist
COMMON_PASSWORDS = {
    'password123', '12345678', 'qwerty123', 'admin123', 'letmein123',
    'welcome123', '123456789', 'password1', 'abc123', 'password'
}

class PasswordStrengthMeter:
    def __init__(self):
        self.special_chars = '!@#$%^&*'
        self.score_weights = {
            'length': 1.0,
            'uppercase': 1.0,
            'lowercase': 1.0,
            'digits': 1.0,
            'special': 1.0,
            'complexity': 1.0
        }

    def check_password_strength(self, password):
        """
        Analyzes password strength and returns a score and feedback.
        """
        if password.lower() in COMMON_PASSWORDS:
            return 0, ["❌ This is a commonly used password. Please choose a unique password."]

        score = 0
        feedback = []

        # Length Check (with graduated scoring)
        if len(password) >= 12:
            score += self.score_weights['length']
        elif len(password) >= 8:
            score += self.score_weights['length'] * 0.5
        else:
            feedback.append("❌ Password should be at least 8 characters long (12+ recommended).")

        # Upper & Lowercase Check
        if re.search(r"[A-Z]", password):
            score += self.score_weights['uppercase'] * 0.5
        else:
            feedback.append("❌ Include uppercase letters.")
        
        if re.search(r"[a-z]", password):
            score += self.score_weights['lowercase'] * 0.5
        else:
            feedback.append("❌ Include lowercase letters.")

        # Digit Check
        if re.search(r"\d", password):
            score += self.score_weights['digits']
        else:
            feedback.append("❌ Add at least one number (0-9).")

        # Special Character Check
        if re.search(f"[{re.escape(self.special_chars)}]", password):
            score += self.score_weights['special']
        else:
            feedback.append(f"❌ Include at least one special character ({self.special_chars}).")

        # Additional Complexity Checks
        if len(set(password)) >= 8:  # Check for character variety
            score += self.score_weights['complexity'] * 0.5
        
        if not re.search(r"(.)\1{2,}", password):  # Check for character repetition
            score += self.score_weights['complexity'] * 0.5
        else:
            feedback.append("❌ Avoid repeating characters (e.g., 'aaa').")

        return score, feedback

    def generate_strong_password(self, length=12):
        """
        Generates a strong password meeting all criteria.
        """
        if length < 8:
            length = 12

        # Ensure at least one of each required character type
        password_chars = [
            random.choice(string.ascii_uppercase),
            random.choice(string.ascii_lowercase),
            random.choice(string.digits),
            random.choice(self.special_chars)
        ]

        # Fill the rest with random characters
        remaining_length = length - len(password_chars)
        all_chars = string.ascii_letters + string.digits + self.special_chars
        password_chars.extend(random.choice(all_chars) for _ in range(remaining_length))

        # Shuffle the password characters
        random.shuffle(password_chars)
        return ''.join(password_chars)

    def get_strength_label(self, score):
        """
        Converts numerical score to strength label.
        """
        if score >= 5:
            return "Strong", "✅"
        elif score >= 3:
            return "Moderate", "⚠️"
        else:
            return "Weak", "❌"

# Set up the Streamlit page
st.set_page_config(
    page_title="Password Strength Meter",
    page_icon="🔒",
    layout="centered"
)

# Initialize the password meter
meter = PasswordStrengthMeter()

# Add title and description
st.title("🔒 Password Strength Meter")
st.markdown("""
This tool helps you evaluate password strength and generate secure passwords.
Check your password strength or generate a new strong password using the options below.
""")

# Create tabs for different functionalities
tab1, tab2 = st.tabs(["Check Password", "Generate Password"])

# Password Strength Check Tab
with tab1:
    st.header("Check Password Strength")
    password = st.text_input("Enter your password:", type="password")
    
    if password:
        score, feedback = meter.check_password_strength(password)
        strength, icon = meter.get_strength_label(score)
        
        # Create a color-coded box for the strength rating
        color = {
            "Strong": "green",
            "Moderate": "orange",
            "Weak": "red"
        }[strength]
        
        st.markdown(f"""
        <div style='padding: 10px; border-radius: 5px; background-color: {color}; color: white;'>
        Password Strength: {icon} {strength} (Score: {score:.1f}/6.0)
        </div>
        """, unsafe_allow_html=True)
        
        if feedback:
            st.markdown("### Improvement Suggestions:")
            for suggestion in feedback:
                st.markdown(suggestion)
        elif strength == "Strong":
            st.success("✅ Excellent! Your password meets all security criteria.")

# Password Generation Tab
with tab2:
    st.header("Generate Strong Password")
    length = st.slider("Password Length", min_value=8, max_value=32, value=12)
    
    if st.button("Generate Password"):
        generated_password = meter.generate_strong_password(length)
        st.code(generated_password, language=None)
        
        # Add a score display for the generated password
        score, _ = meter.check_password_strength(generated_password)
        strength, icon = meter.get_strength_label(score)
        st.markdown(f"Password Strength: {icon} {strength} (Score: {score:.1f}/6.0)")

# Add information about security criteria
with st.expander("Security Criteria"):
    st.markdown("""
    The password strength is evaluated based on:
    - Length (minimum 8 characters, 12+ recommended)
    - Presence of uppercase letters
    - Presence of lowercase letters
    - Presence of numbers
    - Presence of special characters (!@#$%^&*)
    - Character variety
    - Absence of repeated characters
    - Not being a common password
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>

</div>
""", unsafe_allow_html=True) 