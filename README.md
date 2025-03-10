# Password Strength Meter

A Python-based password strength analyzer and generator that helps users create and evaluate secure passwords. Available both as a command-line tool and a web application using Streamlit.

## Features

- Password strength analysis with detailed feedback
- Strong password generation
- Common password blacklist
- Multiple security criteria checks:
  - Password length
  - Uppercase and lowercase letters
  - Numbers
  - Special characters
  - Character variety and repetition
  - Common password detection
- Web interface using Streamlit
- Command-line interface

## Requirements

- Python 3.6 or higher
- Streamlit (for web interface)

## Installation

1. Clone or download this repository
2. Navigate to the project directory
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Web Interface (Streamlit)

Run the Streamlit app:
```bash
streamlit run streamlit_app.py
```

The web interface provides:
- A modern, user-friendly interface
- Password strength checking with visual feedback
- Password generation with customizable length
- Detailed security criteria information

### Command Line Interface

Run the command-line version:
```bash
python password_strength_meter.py
```

### Menu Options

1. **Check password strength**: Analyze the strength of a password
   - Provides a score out of 6.0
   - Shows detailed feedback for improvement
   - Indicates if the password is Weak, Moderate, or Strong

2. **Generate strong password**: Create a secure password
   - Specify desired length (minimum 8 characters)
   - Automatically includes all required character types
   - Ensures random distribution of characters

3. **Exit**: Close the program

## Security Criteria

The password strength is evaluated based on:

- Length (minimum 8 characters, 12+ recommended)
- Presence of uppercase letters
- Presence of lowercase letters
- Presence of numbers
- Presence of special characters (!@#$%^&*)
- Character variety
- Absence of repeated characters
- Not being a common password

## Score Interpretation

- 0-2.9: Weak (❌)
- 3.0-4.9: Moderate (⚠️)
- 5.0-6.0: Strong (✅)

## Deployment

You can deploy this Streamlit app to various platforms:

### Streamlit Cloud (Recommended)
1. Fork this repository to your GitHub account
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Sign in with your GitHub account
4. Deploy the app by selecting your forked repository and the `streamlit_app.py` file

### Local Deployment
1. Install the requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the Streamlit app:
   ```bash
   streamlit run streamlit_app.py
   ```

## Note

This tool is designed for educational purposes and as a general guide for password security. For critical systems, please refer to the latest security standards and guidelines specific to your use case. 