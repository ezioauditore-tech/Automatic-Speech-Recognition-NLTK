import streamlit as st
from speech import speech_to_text

# Streamlit application
st.title("Speech Recognition with Streamlit")

if st.button("Start Recording"):
    st.text("Recording... Speak into your microphone.")
    recognized_text = speech_to_text()
    
    if recognized_text:
        st.write(f"Recognized text: {recognized_text}")
