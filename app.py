# app.py
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Establecer tu clave de API de OpenAI
cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Diccionario de información de países
info_paises = {
    "Estados Unidos": {
        "visa_requerida": False,
        "tipo_de_enchufe": "Tipo A, B",
        "seguridad_del_agua": "Generalmente segura",
        "moneda": "USD",
        "adaptador_de_electricidad": "Tipo A, B"
    },
    "Reino Unido": {
        "visa_requerida": False,
        "tipo_de_enchufe": "Tipo G",
        "seguridad_del_agua": "Generalmente segura",
        "moneda": "GBP",
        "adaptador_de_electricidad": "Tipo G"
    },
    "Francia": {
        "visa_requerida": False,
        "tipo_de_enchufe": "Tipo C, E",
        "seguridad_del_agua": "Generalmente segura",
        "moneda": "EUR",
        "adaptador_de_electricidad": "Tipo C, E"
    },
    "Alemania": {
        "visa_requerida": False,
        "tipo_de_enchufe": "Tipo C, F",
        "seguridad_del_agua": "Generalmente segura",
        "moneda": "EUR",
        "adaptador_de_electricidad": "Tipo C, F"
    },
    "España": {
        "visa_requerida": False,
        "tipo_de_enchufe": "Tipo C, F",
        "seguridad_del_agua": "Generalmente segura",
        "moneda": "EUR",
        "adaptador_de_electricidad": "Tipo C, F"
    },
    # Agregar más países según sea necesario
}

def generar_sugerencias_de_viaje(entrada_usuario):
    # Prompt adicional para cosas que llevar, requisitos de visa, vacunas y adaptadores de electricidad
    prompt = f"Dados los siguientes detalles sobre mi próximo viaje:\n\n{entrada_usuario}\n\nPor favor, proporciona sugerencias de viaje personalizadas, incluyendo cosas que hacer, lugares para alojarse, restaurantes recomendados y cualquier otra información relevante basada en los detalles proporcionados.\n\nAdemás, incluye información sobre cosas que llevar, requisitos de visa, vacunas necesarias y adaptadores de electricidad específicos para el destino."
    respuesta = cliente.chat.completions.create(
        model="gpt-3.5-turbo",  # Especificar el motor GPT-3
        messages=[
            {
                "role": "usuario",
                "content": prompt
            }
        ]
    )
    return respuesta.choices[0].message.content.strip()

def principal():
    st.title("Travalser: Tu Asistente de Viajes Personalizado")

    st.markdown("Bienvenido a Travalser, tu asistente de viajes personalizado. Completa la siguiente información para recibir recomendaciones y sugerencias para tu próximo viaje.")

    # Aquí puedes incluir una breve descripción de la aplicación y su funcionalidad.

    pais_origen = st.text_input("País de Origen")
    ciudad_origen = st.text_input("Ciudad de Origen")
    st.markdown("*Por favor, ingresa tu país y ciudad de origen. Esta información nos ayudará a proporcionar sugerencias más personalizadas.*")
    genero = st.radio("Selecciona Género", ("Masculino", "Femenino"))
    edad = st.slider("Selecciona Edad", 1, 100, 18)
    estilo_viaje = st.selectbox("Selecciona Estilo de Viaje", ("Explorar", "Aventura", "Relax", "Bienestar"))
    pais_destino = st.text_input("País de Destino")
    ciudad_destino = st.text_input("Ciudad de Destino")
    st.markdown("*Por favor, ingresa tu país y ciudad de destino. Esta información nos ayudará a proporcionar sugerencias más personalizadas.*")
    fecha_viaje = st.date_input("Selecciona Fecha de Viaje")
    num_viajeros = st.number_input("Número de Viajeros", min_value=1, value=1)

    if st.button("Planificar Mi Viaje"):
        entrada_usuario = f"- Origen: {pais_origen}, {ciudad_origen}\n- Destino: {pais_destino}, {ciudad_destino}\n- Fechas de Viaje: {fecha_viaje}\n- Estilo de Viaje: {estilo_viaje}\n- Número de Viajeros: {num_viajeros}"
        sugerencias = generar_sugerencias_de_viaje(entrada_usuario)

        st.write("Aquí tienes tus sugerencias de viaje personalizadas:")
        st.write(sugerencias)

        # Muestra información adicional basada en el país de destino
        if pais_destino in info_paises:
            st.write("Información Adicional:")
            st.write(f"- ¿Se requiere Visa?: {'Sí' if info_paises[pais_destino].get('visa_requerida') else 'No'}")
            st.write(f"- Moneda: {info_paises[pais_destino].get('moneda')}")
            st.write(f"- Tipo de Adaptador Eléctrico: {info_paises[pais_destino].get('adaptador_de_electricidad')}")
            st.write(f"- Seguridad del Agua Potable: {info_paises[pais_destino].get('seguridad_del_agua')}")
        else:
            st.write("Información adicional no disponible para este destino.")

if __name__ == "__main__":
    principal()
