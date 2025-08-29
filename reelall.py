# chat_app.py
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# Set your OpenAI API key securely
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are an Effective Instagram Reels copywriting Expert"}]

# Display chat messages
st.title("💬 Chat with OpenAI")
for msg in st.session_state.messages[1:]:  # Skip system prompt
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

instructions = """You are an Effective Instagram Reels copywriting Expert to Generate a detailed prompt in spanish to keep atention until the end on a instagram interview reel from a text-to-text. 

FIRST STEP when ask to do hooks, create 5 winner ideas based on internet search about controversial decisions viral reel to combine massive reach with the strategic intention of getting customers.

Each winner ideas with its respectively 3 best hooks for instagram reels. Explain why are best hooks. Skip the 'create' or 'generate' words, directly output the description as if it's a script to video for social media. From this base prompt: {prompt}. 

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

# Chat input box
if prompt := st.chat_input("Ask me anything..."):
    # Add user's message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response from OpenAI
    with st.chat_message("assistant"):
        response = client.responses.create(
            model="o4-mini-deep-research", #"gpt-4o-mini", #
            tools=[{ "type": "web_search_preview" }],
            input= st.session_state.messages,
            instructions=instructions,
            #store=False
            
        )

    
            
        reply = response.output_text
        st.markdown(reply)
    

    # Add assistant's response to chat history
    st.session_state.messages.append({"role": "assistant", "content": reply})
