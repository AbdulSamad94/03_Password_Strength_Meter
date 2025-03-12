# 🔒 Password Strength Checker

## 📌 Overview
The **Password Strength Checker** is a Streamlit-based web application that evaluates the strength of user-provided passwords and provides suggestions for improvement. It also includes a strong password generator to help users create secure passwords.

## 🚀 Features
- **Password Strength Analysis**: Evaluates passwords based on length, character variety, and complexity.
- **Security Suggestions**: Provides recommendations to improve weak passwords.
- **Password Generator**: Generates strong, random passwords.
- **User-friendly UI**: Styled with custom CSS for both light and dark mode support.

## 🛠️ Technologies Used
- **Python**
- **Streamlit**
- **Regular Expressions (re)**
- **Random module** (for password generation)
- **HTML & CSS** (for custom styling)

## 📥 Installation
To run the Password Strength Checker on your local machine, follow these steps:

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/password-strength-checker.git
   cd password-strength-checker
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```
   
## 📌 How It Works
1. Enter a password in the input field.
2. Click on **Check Strength** to analyze the password.
3. Receive a rating (Weak, Moderate, Strong, or Very Strong) along with suggestions.
4. Click **Generate Password** to get a strong, randomly generated password.

## 🔑 Password Strength Criteria
The strength of a password is determined based on:
- Length (Minimum 12 characters recommended)
- Uppercase and lowercase letter usage
- Inclusion of numbers
- Presence of special characters
- Avoidance of common sequences (e.g., "123", "password")

## 📜 License
This project is licensed under the MIT License.

## 🤝 Contributing
Contributions are welcome! Feel free to submit issues or pull requests.

## 📧 Contact
For any inquiries, reach out at **abdulsamadwork109@gmail.com**.

