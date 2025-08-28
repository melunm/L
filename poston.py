

import streamlit as st
from PIL import Image
import openai
import base64
import os
from dotenv import load_dotenv
from datetime import datetime

# Set up folders and load environment variables
DESCRIPTION_FOLDER = "description"
os.makedirs(DESCRIPTION_FOLDER, exist_ok=True)

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")



# Define your credentials (hardcoded for simplicity)
username_correct = os.getenv("USERNAME")
password_correct = os.getenv("PASSWORD")

# 1. Create the login form at the beginning
def login():
    st.set_page_config(page_title="LUNA", layout="centered")
    st.title("Login to LUNA")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if username == username_correct and password == password_correct:
            st.success("Logged in successfully!")
            return True
        else:
            st.error("Incorrect username or password.")
            return False

# 2. Main App logic: Check if user is authenticated
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if st.session_state.logged_in:
    # App content appears after successful login
    # Initialize chat history





    st.set_page_config(page_title="LUNA Image", layout="centered")
    st.title("LUNA Image Description")
    st.write("Sube cualquier imagen y deja el trabajo a la inteligencia artificial")

    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

    def image_to_base64(img_file):
        img_file.seek(0)
        return base64.b64encode(img_file.read()).decode('utf-8')

    DESCRIPTION_TEMPLATE = """
    You are a helpful assistant that provides detailed descriptions of images. When given an image, you should describe it in extreme detail, mentioning colors, objects, textures, people (if any), and any other relevant features visible in the image. Please provide a comprehensive analysis of the image.


    """


    def get_image_description(image_b64):
        try:
            response = openai.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[
                    {"role": "system", "content": DESCRIPTION_TEMPLATE},
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": "Describe this image in extreme detail according to the provided structure and template."},
                            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_b64}"}}
                        ]
                    }
                ],
                max_tokens=4000
            )
            return response.choices[0].message.content  # Correct way to access the content
        except Exception as e:
            return f"Error from OpenAI API: {str(e)}"

    # Handle image upload and description
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)

        # Convert image to base64
        image_b64 = image_to_base64(uploaded_file)

        # Get the description of the image
        with st.spinner("Generating image description..."):
            image_description = get_image_description(image_b64)

        st.subheader("Image Description")
        st.write(image_description)

        # Chat interface for questions
        if "conversation_history" not in st.session_state:
            st.session_state.conversation_history = []

        # Display previous conversation
        for chat in st.session_state.conversation_history:
            st.write(f"**{chat['role']}**: {chat['message']}")

        user_question = st.text_input("Ask a question about the image:")

        if user_question:
            # Append the user question to the conversation history
            st.session_state.conversation_history.append({"role": "user", "message": user_question})

            # Get the answer from GPT-4
            try:
                response = openai.chat.completions.create(
                    model="gpt-4.1-mini",
                    messages=[
                        #{"role": "system", "content": DESCRIPTION_TEMPLATE},
                        {"role": "user", "content": image_description},  # Provide image description as context
                        {"role": "user", "content": user_question}  # The user's question
                    ],
                    max_tokens=4000
                )
                # Correct way to access the answer content
                response.choices[0].message.content  # Access content correctly
                st.session_state.conversation_history.append({"role": "assistant", "message": response.choices[0].message.content })

                # Display the answer from GPT-4
                #st.write(f"**Assistant**: {response}")

            except Exception as e:
                st.write(f"Error occurred while getting the answer: {str(e)}")

                #do code to create a html, css site to sell beachwear and accesories using this image and its description.
    #add a shopping cart, checkout, or backend, you'll want JavaScript








else:
    # Show login form if user is not logged in
    if login():
        # After successful login, set session state and refresh
        st.session_state.logged_in = True
        st.rerun()  # This refreshes the page and opens the app automatically
    else:
        # Inform the user that they need to log in
        st.info("Please log in to continue.")
