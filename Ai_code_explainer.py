import os
from dotenv import load_dotenv
import streamlit as st
from google import genai

load_dotenv()

st.set_page_config(
    page_title="AI Code Explainer",
    page_icon="🤖",
    layout="wide"
)

API_KEY = os.getenv("GEMINI_API_KEY")

# Create Gemini client
try:
    client = genai.Client(api_key=API_KEY)
except Exception as e:
    st.error(f"Gemini Client Error: {e}")
    st.stop()

st.title("🤖 AI Code Explainer")
st.write("Paste your Python code below and click **Explain Code**.")

# Code input
code = st.text_area(
    "Python Code",
    height=300,
    placeholder="Paste your Python code here..."
)

# Explain button
if st.button("Explain Code"):

    if not code.strip():
        st.warning("Please enter some Python code.")
    else:

        prompt = f"""
You are an expert Python programmer.

Explain the following code in simple English.

Provide:

1. Purpose of the code
2. Line-by-line explanation
3. Expected Output
4. Time Complexity
5. Space Complexity
6. Suggestions for Improvement

Python Code:

{code}
"""

        with st.spinner("Generating explanation..."):

            try:

                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt
                )

                st.success("Explanation Generated Successfully!")

                st.markdown(response.text)

            except Exception as e:
                st.error(f"Error: {e}")