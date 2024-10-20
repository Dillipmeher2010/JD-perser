import streamlit as st
import google.generativeai as genai

# Header for the Streamlit app
st.header("JD Parser")

# Retrieve the API key from Streamlit secrets
GOOGLE_API_KEY = st.secrets["GEMINI_API_KEY"]

# Configure the Google Generative AI API with your API key
genai.configure(api_key=GOOGLE_API_KEY)

# Text input for user prompt
user_input = st.text_area("Enter your prompt to generate content:")

prompt = f"""
Analyze the following Job Description:

1. Extract the top keywords.
2. Suggest a learning plan based on the skills required.
3. Provide the top interview questions a candidate might face.

Job Description: {user_input}
"""

# Button to submit the prompt
if st.button("Generate"):
    if user_input:
        # Initialize the model
        model = genai.GenerativeModel('gemini-pro')  # Assuming this is the correct model
        try:
            # Generate content based on the user's input
            response = model.generate_content(prompt)
            
            # Display the generated content
            st.write("Generated Content:")
            st.write(response.text)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.error("Please enter a prompt.")
