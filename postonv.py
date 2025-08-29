

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

    CONTENT = """You are an Effective Instagram Reels copywriting Expert"""
    
    DESCRIPTION_TEMPLATE ="""You are an Effective Instagram Reels copywriting Expert to Generate a detailed prompt in spanish to keep atention until the end on a instagram interview reel from a text-to-text. 

    FIRST STEP when ask to do hooks, create 5 winner ideas based on the image and a controversial decisions viral reel to combine massive reach with the strategic intention of getting customers.

    Each winner ideas with its respectively 1 best hooks for instagram reels. Explain why are best hooks. Skip the 'create' or 'generate' words, directly output the description as if it's a script to video for social media. From this base prompt: {prompt}. 

    To create hooks use a powerful, quick phrase that sparks emotion and creates curiosity. 
    The hook with a visual element, using a viral reel reference or a clear promise.
    The hook based on desire of health, money, personal developement and spiritual developement. 

    SECOND STEP when ask to develop ALL generated hooks to create a detail interview script for 60 seconds video with each hook to keep atention until the end. 
    When you write theses interview scripts develop the winner idea including before each time someone speak the Curiosity points to keep attention or the Loops to give the expectation some will happen. Curiosity Points trigger intrigue and keep the viewer captivated. These include phrases like 'only 1% know this,' sudden shifts in music, rapid zooms, or unexpected scene changes. Loops are a strategy that disrupt the pattern and build anticipation, keeping the viewer engaged until the very end. Examples of Loops include phrases like 'and at the end, I’ll reveal the most important thing,' a pause right before a powerful statement, or showing something on screen without explaining it, like an unfinished word.


    Use as example: interview script for instagram reel en espanol. busca un hook mejor que este: 

    Part Hook:

    [Inicio: Tú y tu abuela están en la cocina, rodeadas de una atmósfera hogareña. Ambas sonríen a la cámara.]
    Include loops o Curiosity point por el Entrevistador (fuera de cámara): “Dicen que es cosa de brujas, pero esa mascarilla casera cambió tu piel para siempre. ¿Cuál es el secreto?”

    Part Context or setup: Quickly immerse the viewer in the story of the video by the viewer feel implicated in the story.
    The contexte has information to understand the outcome.

    Conflict or loss or downfall in story: here we feel the emotional weight, conveying failure, hopelessness, or rupture. 

    Tú (riendo, sorprendida): “¡Uf, sí! Yo también pensaba que era cuento. Al principio me burlaba de la idea… pero luego resultó ser un milagro para mi piel seca.”

    Change or Insight or turning point: This is where the rebirth begins, the mission. The click that sparks action to solve it.

    [Corte rápido: Cámara enfoca de cerca los ingredientes naturales sobre la mesa: avena molida, miel pura y un chorrito de aceite de almendras.]
    Include loops o Curiosity point por el Entrevistador (voz en off): “¿Qué hay en esa pócima mágica?”
    Tú (señalando los ingredientes): “Mi abuela lo llamaba su ‘pócima de belleza’. Es una mezcla ancestral… Dicen que es cosa de brujas, pero créeme, ¡es un secreto familiar que me dejó la piel increíble!”

    Part Resolution or outcome or inspiration: an epic message that inspires.
    Resolution or outcome is what establishes your authority in the field. It makes you the go-to reference for those eager to learn or improve. It strengthens your position as an expert and sets you apart from the crowd.

    [Corte: Mezclas y preparas la mascarilla. Trituras la avena, añades la miel y el aceite de almendras en un bol.]
    Incluso loops o Curiosity point por Tú (voz en off, mientras mezclas): “Avena, miel y un chorrito de aceite de almendras. Hago la mezcla hasta que tiene textura cremosa. Luego me la aplico en la cara limpita y dejo que haga efecto…”
    (El vídeo muestra el proceso de aplicar la mascarilla, sin revelar el resultado final inmediatamente.)

    [Corte rápido: Te retiras la mascarilla, sorprendida, mirando el espejo mientras pasas la mano por tu piel. Se nota más suave e hidratada.]
    Tú (emocionada, mirando a cámara): “¡Wow! No lo esperaba… ¡mi piel quedó como nueva! Ese truco de abuela sí que funciona.”

    Part Circular closure or viral phrase: A line to close powerfully, emotionally connect, and spark virality.
    or A powerful ending that strikes deep, connects hearts, and spreads like wildfire.
    Circular closure or viral phrase offers real value, actionable steps, and connect it to desire or something deeply emotional.

    [Corte final: Tú y tu abuela brindan con tazas de té, sonriendo cómplices a la cámara.]
    Incluso loops o Curiosity point por el Entrevistador (fuera de cámara): “Nada mal para una receta de ‘bruja’, ¿no? ¿Compartes la receta secreta?”
    Tú (guiñando un ojo a cámara): “¿Quieren todos los detalles de esta mascarilla milagrosa? 

    Part The call to action needs to be clear and specific to drive this traffic to sell or follow: 

    Tú: Comenten ‘INFO’ y se los envío. ¡No se la pueden perder!”
    (Texto en pantalla al final: “Comenta ‘INFO’ para conocer la receta secreta ✨” aparece mientras saludas con una sonrisa.)

    Explicación del Guion:

    IDEA GANADORA: Usa el contraste entre lo moderno y lo tradicional: una mascarilla casera “de brujas” (antigua y misteriosa) que realmente cura la piel seca. Se basa en la figura confiable de la abuela para dar credibilidad al remedio. La persona entrevistada inicialmente duda del tratamiento, lo que refleja la actitud del público escéptico, pero luego muestra los resultados sorprendentes.
    PUNTOS DE CURIOSIDAD: Se explotan frases como “Dicen que es cosa de brujas” y “pócima mágica” que enganchan a la audiencia desde el principio. Mencionar “secreto familiar” y ver los ingredientes naturales genera intriga inmediata. Cada intervención del entrevistador (“¿Cuál es el secreto?”, “¿Qué hay en esa pócima mágica?”, “¿Compartes la receta secreta?”) mantiene la atención, pues promete revelar un misterio. Además, no mostramos el resultado final de inmediato (la aplicación de la mascarilla está en un corte), lo que hace que la audiencia espere para ver “el antes y después”.
    LOOPS: Se usan frases que dan pistas pero no revelan todo (“¡créeme, es un secreto familiar!”, “espera a ver esto… ¡mi piel quedó como nueva!”). Estos pequeños cliffhangers, combinados con cortes dinámicos, mantienen la tensión. El guion termina con una llamada a la acción (“comenta ‘INFO’ para la receta”), dejando la historia abierta hasta que el espectador interactúe. Esto garantiza que la audiencia se quede hasta el final y se implique con el contenido.

    Explain for each script Winner Idea, Curiosity points to keep attention, Loops to give the expectation some will happen that are created.
    """ 


    def get_image_description(image_b64):
        try:
            response = openai.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[
                    {"role": "system", "content": CONTENT},
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": DESCRIPTION_TEMPLATE},
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
