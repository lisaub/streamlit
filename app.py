# app.py
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set your OpenAI API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Placeholder country information dictionary
country_info = {
    "United States": {
        "visa_required": False,
        "plug_type": "Type A, B",
        "water_safety": "Generally safe",
        "currency": "USD",
        "electricity_adapter": "Type A, B"
    },
    "United Kingdom": {
        "visa_required": False,
        "plug_type": "Type G",
        "water_safety": "Generally safe",
        "currency": "GBP",
        "electricity_adapter": "Type G"
    },
    "France": {
        "visa_required": False,
        "plug_type": "Type C, E",
        "water_safety": "Generally safe",
        "currency": "EUR",
        "electricity_adapter": "Type C, E"
    },
    "Germany": {
        "visa_required": False,
        "plug_type": "Type C, F",
        "water_safety": "Generally safe",
        "currency": "EUR",
        "electricity_adapter": "Type C, F"
    },
    "Spain": {
        "visa_required": False,
        "plug_type": "Type C, F",
        "water_safety": "Generally safe",
        "currency": "EUR",
        "electricity_adapter": "Type C, F"
    },
    # Add more countries as needed
}

def generate_travel_suggestions(user_input):
    # Additional prompt for things to pack, visa requirements, vaccinations, and electricity adapters
    prompt = f"Given the following details about my upcoming trip:\n\n{user_input}\n\nPlease provide personalized travel suggestions including things to do, places to stay, recommended restaurants, and any other relevant information based on the given details.\n\nAdditionally, please include information on things to pack, visa requirements, vaccinations needed, and specific electricity adapters for the destination."
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Specify the GPT-3 engine
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.choices[0].message.content.strip()

def main():
    st.title("Travalser: Tu Asistente de Viajes Personalizado")

    st.markdown("Bienvenido a Travalser, tu asistente de viajes personalizado. Completa la siguiente información para recibir recomendaciones y sugerencias para tu próximo viaje.")

    # Aquí puedes incluir una breve descripción de la aplicación y su funcionalidad.

    origin_country = st.text_input("País de Origen")
    origin_city = st.text_input("Ciudad de Origen")
    st.markdown("*Por favor, ingresa tu país y ciudad de origen. Esta información nos ayudará a proporcionar sugerencias más personalizadas.*")
    gender = st.radio("Selecciona Género", ("Masculino", "Femenino"))
    age = st.slider("Selecciona Edad", 1, 100, 18)
    travel_style = st.selectbox("Selecciona Estilo de Viaje", ("Explorar", "Aventura", "Relax", "Bienestar"))
    destination_country = st.text_input("País de Destino")
    destination_city = st.text_input("Ciudad de Destino")
    st.markdown("*Por favor, ingresa tu país y ciudad de destino. Esta información nos ayudará a proporcionar sugerencias más personalizadas.*")
    travel_date = st.date_input("Selecciona Fecha de Viaje")
    num_travelers = st.number_input("Número de Viajeros", min_value=1, value=1)

    if st.button("Planificar Mi Viaje"):
        user_input = f"- Origen: {origin_country}, {origin_city}\n- Destino: {destination_country}, {destination_city}\n- Fechas de Viaje: {travel_date}\n- Estilo de Viaje: {travel_style}\n- Número de Viajeros: {num_travelers}"
        suggestions = generate_travel_suggestions(user_input)

        st.write("Aquí tienes tus sugerencias de viaje personalizadas:")
        st.write(suggestions)

        # Muestra información adicional basada en el país de destino
        if destination_country in country_info:
            st.write("Información Adicional:")
            st.write(f"- ¿Se requiere Visa?: {'Sí' if country_info[destination_country].get('visa_required') else 'No'}")
            st.write(f"- Moneda: {country_info[destination_country].get('currency')}")
            st.write(f"- Tipo de Adaptador Eléctrico: {country_info[destination_country].get('electricity_adapter')}")
            st.write(f"- Seguridad del Agua Potable: {country_info[destination_country].get('water_safety')}")
        else:
            st.write("Información adicional no disponible para este destino.")

if __name__ == "__main__":
    main()