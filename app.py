import streamlit as st 
st.header("JD Parser")

# Take long text input from the user
user_input = st.text_area("Enter One Job Description:")

# Button to submit the input
if st.button("Submit"):
    # Display the user input concatenated with a message
    st.write(f"Job Description received: {user_input}")