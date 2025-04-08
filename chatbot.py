import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("MyApiKey")

# Configura tu API Key aquí o usa variables de entorno
client = OpenAI(api_key=api_key)

# Título de la app
st.title("Hola, soy un Chatbot de Contabilidad y Finanzas")
st.write("Puedes preguntarme cualquier cosa relacionada a la contabilidad y finanzas")
st.write("Me asegurare de solucionar cualquier duda de manera clara y concisa")

# Inicializa los mensajes de la conversación
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "Eres un experto en contabilidad y finanzas. Responde como asesor financiero profesional con explicaciones claras y prácticas."}
    ]

# Mostrar mensajes previos
for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Entrada del usuario
user_input = st.chat_input("Hazme una pregunta sobre contabilidad...")

if user_input:
    # Agrega el mensaje del usuario
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Llama a la API de OpenAI
    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=st.session_state.messages
        )
        reply = completion.choices[0].message.content

        # Agrega la respuesta al estado
        st.session_state.messages.append({"role": "assistant", "content": reply})
        with st.chat_message("assistant"):
            st.markdown(reply)

    except Exception as e:
        st.error(f"❌ Error al generar la respuesta: {e}")
