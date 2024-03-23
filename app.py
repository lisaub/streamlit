import streamlit as st
import streamlit.secrets as secrets
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Get your OpenAI API key from secrets
api_key = secrets['openai']['api_key']

# Set your OpenAI API key
cliente = OpenAI(api_key)

# Set your OpenAI API key
# cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Dictionary of country information
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
    # Add more countries as needed
}

def generar_sugerencias_de_viaje(entrada_usuario):
    # Additional prompt for things to bring, visa requirements, vaccines, and electricity adapters
    prompt = f"Dados los siguientes detalles sobre mi próximo viaje:\n\n{entrada_usuario}\n\nPor favor, proporciona sugerencias de viaje personalizadas, incluyendo cosas que hacer, lugares para alojarse, restaurantes recomendados y cualquier otra información relevante basada en los detalles proporcionados.\n\nAdemás, incluye información sobre cosas que llevar, requisitos de visa, vacunas necesarias y adaptadores de electricidad específicos para el destino."
    respuesta = cliente.chat.completions.create(
        model="gpt-3.5-turbo",  # Specify the GPT-3 engine
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

    st.markdown("### Cómo Funciona:")
    st.markdown("Travalser, tu asistente de viajes personalizado, aprovecha la tecnología avanzada de IA para adaptar recomendaciones de viaje a tus preferencias. Simplemente ingresa detalles como tus países de origen y destino, fechas de viaje y estilo de viaje. Una vez que presiones 'Planificar Mi Viaje', Travalser generará sugerencias de viaje personalizadas que incluyen actividades, alojamientos, opciones de restaurantes y más. Además, proporciona información de viaje esencial como requisitos de visa, moneda, tipos de adaptadores eléctricos y seguridad del agua para tu destino. Espera sugerencias perspicaces y personalizadas que mejoren tu experiencia de viaje, haciendo que cada viaje sea inolvidable.")

    pais_origen = st.text_input("País de Origen")
    ciudad_origen = st.text_input("Ciudad de Origen")
    st.markdown("*Por favor, ingresa tu país y ciudad de origen. Esta información nos ayudará a proporcionar sugerencias más personalizadas.*")
    genero = st.radio("Selecciona Género", ("Masculino", "Femenino"))
    edad = st.slider("Selecciona Edad", 1, 100, 18)
    estilo_viaje = st.selectbox("Selecciona Estilo de Viaje", ("Explorar", "Aventura", "Relax", "Bienestar"))
    pais_destino = st.selectbox("País de Destino", options=list(info_paises.keys()), index=0)
    ciudad_destino = st.text_input("Ciudad de Destino")
    st.markdown("*Por favor, ingresa tu país y ciudad de destino. Esta información nos ayudará a proporcionar sugerencias más personalizadas.*")
    fecha_viaje = st.date_input("Selecciona Fecha de Viaje")
    num_viajeros = st.number_input("Número de Viajeros", min_value=1, value=1)

    if st.button("Planificar Mi Viaje"):
        # Append age and gender to the entrada_usuario string
        entrada_usuario = f"- Origen: {pais_origen}, {ciudad_origen}\n- Destino: {pais_destino}, {ciudad_destino}\n- Fechas de Viaje: {fecha_viaje}\n- Estilo de Viaje: {estilo_viaje}\n- Número de Viajeros: {num_viajeros}\n- Género: {genero}\n- Edad: {edad}"

        st.write("Detalles de tu Viaje:")
        st.write(entrada_usuario)

        sugerencias = generar_sugerencias_de_viaje(entrada_usuario)

        st.write("Aquí tienes tus sugerencias de viaje personalizadas:")
        st.write(sugerencias)

        # Show additional information based on the destination country
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
