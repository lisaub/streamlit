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
    st.title("Travel Helper")

    origin_country = st.text_input("Country of Origin")
    origin_city = st.text_input("City of Origin")
    st.markdown("*Please enter your country and city of origin. This information will help us provide more tailored suggestions.*")
    gender = st.radio("Select Gender", ("Male", "Female"))
    age = st.slider("Select Age", 1, 100, 18)
    travel_style = st.selectbox("Select Travel Style", ("Explore", "Adventure", "Relax", "Wellness"))
    destination_country = st.text_input("Destination Country")
    destination_city = st.text_input("Destination City")
    st.markdown("*Please enter your destination country and city. This information will help us provide more tailored suggestions.*")
    travel_date = st.date_input("Select Travel Date")
    num_travelers = st.number_input("Number of Travelers", min_value=1, value=1)

    if st.button("Plan My Trip"):
        user_input = f"- Origin: {origin_country}, {origin_city}\n- Destination: {destination_country}, {destination_city}\n- Travel Dates: {travel_date}\n- Travel Style: {travel_style}\n- Number of Travelers: {num_travelers}"
        suggestions = generate_travel_suggestions(user_input)

        st.write("Here are your personalized travel suggestions:")
        st.write(suggestions)

        # Display additional information based on destination country
        if destination_country in country_info:
            st.write("Additional Information:")
            st.write(f"- Visa Required: {'Yes' if country_info[destination_country].get('visa_required') else 'No'}")
            st.write(f"- Currency: {country_info[destination_country].get('currency')}")
            st.write(f"- Electricity Adapter Type: {country_info[destination_country].get('electricity_adapter')}")
            st.write(f"- Drinking Water Safety: {country_info[destination_country].get('water_safety')}")
        else:
            st.write("Additional information not available for this destination.")

if __name__ == "__main__":
    main()
