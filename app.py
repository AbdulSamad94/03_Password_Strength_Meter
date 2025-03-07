import streamlit as st
import re
import random
import string

st.set_page_config(
    page_title="Password Strength Checker", page_icon="🔒", layout="centered"
)

# --- Custom CSS for Enhanced Styling ---
st.markdown(
    """
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f4f4f4;
            color: #333;
        }
        .stApp {
            background-color: transparent;
        }
        .title {
            text-align: center;
            font-size: 2.8rem;
            font-weight: bold;
            color: #2c3e50;
            margin-bottom: 1.5rem;
        }
        .password-input {
            background-color: #fff;
            border: 2px solid #ddd;
            border-radius: 8px;
            padding: 0.8rem 1rem;
            margin-bottom: 1rem;
            width: 100%;
            box-sizing: border-box;
        }
        .password-input:focus {
            outline: none;
            border-color: #3498db;
            box-shadow: 0 0 8px rgba(52, 152, 219, 0.4);
        }
        .check-button {
            background-color: #3498db;
            color: white;
            border: none;
            border-radius: 8px;
            padding: 0.8rem 1.5rem;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .check-button:hover {
            background-color: #2980b9;
        }
        .result-box {
            border-radius: 8px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        .result-box.success {
            background-color: #e8f8e8;
            border: 1px solid #2ecc71;
        }
        .result-box.info {
            background-color: #e0f2f7;
            border: 1px solid #3498db;
        }
        .result-box.warning {
            background-color: #fff8e1;
            border: 1px solid #f39c12;
        }
        .result-box.error {
            background-color: #ffebee;
            border: 1px solid #e74c3c;
        }
        .suggestion-list {
            list-style-type: disc;
            padding-left: 2rem;
        }
        .suggestion-list li {
            margin-bottom: 0.5rem;
        }
        .generate-button {
            background-color: #27ae60;
            color: white;
            border: none;
            border-radius: 8px;
            padding: 0.8rem 1.5rem;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .generate-button:hover {
            background-color: #1e8449;
        }
        .password-box {
            background-color: #f0f0f0;
            border-radius: 8px;
            padding: 0.8rem;
            font-family: monospace;
            overflow-wrap: break-word;
            margin-top: 0.5rem;
        }
        .dark-mode {
            background-color: #1e1e1e;
            color: #eee;
        }
        .dark-mode .password-input, .dark-mode .password-box {
            background-color: #333;
            border-color: #666;
            color:#fff
        }
        .dark-mode .result-box.success {
            background-color: #223B22;
            border: 1px solid #2ecc71;
        }
        .dark-mode .result-box.info {
            background-color: #18394A;
            border: 1px solid #3498db;
        }
        .dark-mode .result-box.warning {
            background-color: #474128;
            border: 1px solid #f39c12;
        }
        .dark-mode .result-box.error {
            background-color: #3F2221;
            border: 1px solid #e74c3c;
        }
        .dark-mode .check-button {
            background-color:#2980b9;
        }
        .dark-mode .generate-button {
            background-color:#1e8449
        }

        @media (prefers-color-scheme: dark) {
          body {
            background-color: #1e1e1e;
            color: #eee;
          }
          .stApp {
            background-color: transparent;
          }

          .title {
            color: #eee;
          }
          .password-input, .password-box {
            background-color: #333;
            border-color: #666;
            color:#fff
          }
          .result-box.success {
              background-color: #223B22;
              border: 1px solid #2ecc71;
          }
          .result-box.info {
              background-color: #18394A;
              border: 1px solid #3498db;
          }
          .result-box.warning {
              background-color: #474128;
              border: 1px solid #f39c12;
          }
          .result-box.error {
              background-color: #3F2221;
              border: 1px solid #e74c3c;
          }
          .check-button {
            background-color:#2980b9;
          }
          .generate-button {
            background-color:#1e8449
          }
        }
    </style>
    """,
    unsafe_allow_html=True,
)
# --- End of Custom CSS ---

st.markdown(
    "<h1 class='title'>🔐 Password Strength Checker</h1>", unsafe_allow_html=True
)

# --- Password Input ---
password = st.text_input(
    "Enter your password",
    type="password",
    key="password_input",
    placeholder="Type your password here",
    label_visibility="collapsed",
    help="Type your password here",
)


# --- Password strength checker ---
def password_checker(password):
    score = 0
    suggestions = []

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        suggestions.append("Be at least 12 characters long for better security.")

    if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Contain both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Include at least one digit (0-9).")

    if re.search(r"[!@#$%^&*()_+\-=\[\]{};':\\\"|,.<>?/]", password):
        score += 1
    else:
        suggestions.append("Include at least one special character (!@#$%^&*).")

    if not re.search(r"(123|abc|password|qwerty)", password, re.IGNORECASE):
        score += 1
    else:
        suggestions.append("Avoid common sequences like '123', 'abc', or 'password'.")

    return score, suggestions


# --- Password generation ---
def generate_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(characters) for _ in range(length))


# --- Check Strength Button ---
if st.button(
    "Check Strength",
    key="check_strength_button",
    help="Click to check the strength of your password",
    type="primary",
):
    if password:
        score, suggestions = password_checker(password)
        st.markdown(
            "<h2 class='title'>🔍 Password Analysis</h2>", unsafe_allow_html=True
        )

        if score >= 5:
            st.markdown(
                "<div class='result-box success'>🎉 Congratulations! Your password is <b>very strong</b>.</div>",
                unsafe_allow_html=True,
            )
        elif score == 4:
            st.markdown(
                "<div class='result-box info'>✅ Your password is <b>strong</b>, but there's room for improvement.</div>",
                unsafe_allow_html=True,
            )
        elif score == 3:
            st.markdown(
                "<div class='result-box warning'>⚠️ Your password is <b>moderate</b>. Consider improving it.</div>",
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                "<div class='result-box error'>❌ Your password is <b>weak</b>. It needs significant improvement.</div>",
                unsafe_allow_html=True,
            )

        if suggestions:
            st.subheader("🛠️ Suggestions to Improve Your Password")
            st.markdown(
                "<ul class='suggestion-list'>{}</ul>".format(
                    "".join(f"<li>{s}</li>" for s in suggestions)
                ),
                unsafe_allow_html=True,
            )
    else:
        st.error("Please enter a password to check its strength.")

st.markdown("---")

st.subheader("🔑 Generate a Strong Password")
if st.button(
    "Generate Password",
    key="generate_password_button",
    help="Click to generate a new strong password",
    type="secondary",
):
    strong_password = generate_password()
    st.markdown(
        f"<div class='password-box'>{strong_password}</div>", unsafe_allow_html=True
    )
