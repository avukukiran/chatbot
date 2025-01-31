import streamlit as st
from openai import OpenAI

# Show title and description.
st.title("💬 Chatbot")

# Securely get the API key from user input
# openai_api_key = st.text_input("Enter your OpenAI API key:", type="password")
openai_api_key="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"

if not openai_api_key:
    st.info("Please enter your OpenAI API key to continue.", icon="🗝️")
else:
    # Create an OpenAI client securely
    client = OpenAI(api_key=openai_api_key)

    # Initialize session state for chat messages
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input field
    if prompt := st.chat_input("What is up?"):
        # Store and display user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate response using OpenAI API
        stream = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
            stream=True,
        )

        # Stream the response and store it
        with st.chat_message("assistant"):
            response = st.write_stream(stream)
        st.session_state.messages.append({"role": "assistant", "content": response})
