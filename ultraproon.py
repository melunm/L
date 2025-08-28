

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





    import os
    import base64
    import time
    import requests
    from PIL import Image
    from io import BytesIO
    import streamlit as st
    from dotenv import load_dotenv
    from langchain_groq import ChatGroq
    from langchain_core.prompts import PromptTemplate

    # Load environment variables from a .env file
    load_dotenv()

    # Initialize the ChatGroq model
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )

    # Define the prompt template for generating detailed prompts
    prompt_template = PromptTemplate.from_template(
        "Generate a detailed prompt from a text-to-image model. Skip the 'create' or 'generate' words, directly output the description as if it's a caption of an image. From this base prompt: {base_prompt}"
    )

    # Set up the pipeline (chain)
    chain = prompt_template | llm

    # Streamlit UI setup
    st.title("LUNA")

    # Input field for the user to provide a base prompt
    base_prompt = st.text_input("Enter a base prompt:", value="write")

    # Button to trigger the image generation
    if st.button("Generate Image"):
        if base_prompt:
            # Generate detailed prompt using the provided base prompt
            with st.spinner("Generating detailed prompt..."):
                response = chain.invoke({"base_prompt": base_prompt})
                detailed_prompt = response.content
            
            # Display the detailed prompt generated
            st.write("### Detailed Prompt:")
            st.write(detailed_prompt)

            # Make API call to generate image using detailed prompt
            try:
                response = requests.post(
                    'https://api.bfl.ai/v1/flux-pro-1.1-ultra',  
                    headers={
                        'accept': 'application/json',
                        'x-key': os.environ.get("BFL_API_KEY"),
                        'Content-Type': 'application/json',
                    },
                    json={
                        "raw": True, #False More stylized or enhanced visuals True More natural, camera-like image output
                        'prompt': base_prompt, #detailed_prompt,
                        'width': 2048,#
                        'height': 2048,#
                        "seed": 42,
                        "aspect_ratio": "9:16", # "16:9" #CHANGE RATIO
                        "safety_tolerance": 2,
                        "output_format": "jpeg",
                        "prompt_upsampling": "false"
                        #"raw": false,
                        #"image_prompt": "",
                        #"image_prompt_strength": 0.1,
                        #"webhook_url": "https://delivery-us1.bfl.ai/results/8b18769535d84035996e0df19b8ac2d2/sample.jpeg?se=2025-05-10T04%3A13%3A41Z&sp=r&sv=2024-11-04&sr=b&rsct=image/jpeg&sig=gveQliHDl7SCT4/nn9DMxbDQDdi88%2B3iSCQIXIaXUfw%3D",
                        #"webhook_secret": ""

                    },
                ).json()

                if 'id' in response:
                    request_id = response["id"]
                    st.success(f"Image generation started, request ID: {request_id}")
                    
                    # Polling the API to check when the image is ready
                    while True:
                        time.sleep(0.5)
                        result = requests.get(
                            'https://api.us1.bfl.ai/v1/get_result',
                            headers={
                                'accept': 'application/json',
                                'x-key': os.environ.get("BFL_API_KEY"),
                            },
                            params={
                                'id': request_id,
                            },
                        ).json()

                        if result["status"] == "Ready":
                            image_data = result['result']['sample']
                            
                            # Check if the image_data is a URL or base64 string
                            if image_data.startswith('http'):
                                # If it's a URL, download the image
                                try:
                                    image_response = requests.get(image_data)
                                    image = Image.open(BytesIO(image_response.content))
                                    st.image(image, caption="Generated Image", width='stretch')
                                    st.success("Image successfully downloaded from URL.")
                                except Exception as e:
                                    st.error(f"Error downloading image from URL: {e}")
                            else:
                                # If it's base64, decode the base64 string
                                try:
                                    image_bytes = base64.b64decode(image_data)
                                    image = Image.open(BytesIO(image_bytes))
                                    st.image(image, caption="Generated Image", width='stretch')
                                    st.success("Image successfully decoded from base64.")
                                except Exception as e:
                                    st.error(f"Error decoding image: {e}")
                            


                                    # Print the image URL
                                st.write(f"Image URL: {image_data}")



                                st.success(f"Prompt : {prompt_path}")


                                


                            break  # Exit the loop once the image is processed
                        else:
                            st.write(f"Status: {result['status']}. Waiting for image to be ready...")
                else:
                    st.error("Failed to generate image. Please try again.")
            
            except Exception as e:
                st.error(f"An error occurred during image generation: {e}")
        else:
            st.error("Please enter a valid base prompt.")





else:
    # Show login form if user is not logged in
    if login():
        # After successful login, set session state and refresh
        st.session_state.logged_in = True
        st.rerun()  # This refreshes the page and opens the app automatically
    else:
        # Inform the user that they need to log in
        st.info("Please log in to continue.")
