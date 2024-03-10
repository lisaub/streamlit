import streamlit as st

# Define a dictionary to store country-specific information
country_info = {
    "United States": {
        "visa_required": False,
        "plug_type": "Type A, B",
        "water_safety": "Generally safe"
    },
    "United Kingdom": {
        "visa_required": False,
        "plug_type": "Type G",
        "water_safety": "Generally safe"
    },
    "France": {
        "visa_required": False,
        "plug_type": "Type C, E",
        "water_safety": "Generally safe"
    },
    "Germany": {
        "visa_required": False,
        "plug_type": "Type C, F",
        "water_safety": "Generally safe"
    },
    "Spain": {
        "visa_required": False,
        "plug_type": "Type C, F",
        "water_safety": "Generally safe"
    },
    # Add more countries as needed
}

def main():
    st.title("Travel Helper")

    origin_country = st.text_input("Country of Origin")
    st.markdown("*Please enter your country of origin. This information will help us provide more tailored suggestions based on what you're accustomed to.*")
    gender = st.radio("Select Gender", ("Male", "Female"))
    age = st.slider("Select Age", 1, 100, 18)
    travel_style = st.selectbox("Select Travel Style", ("Explore", "Adventure", "Relax", "Wellness"))
    destination = st.text_input("Enter Destination")
    travel_date = st.date_input("Select Travel Date")
    num_travelers = st.number_input("Number of Travelers", min_value=1, value=1)

    if st.button("Plan My Trip"):
        st.write(f"Gender: {gender}")
        st.write(f"Age: {age}")
        st.write(f"Travel Style: {travel_style}")
        st.write(f"Destination: {destination}")
        st.write(f"Travel Date: {travel_date}")
        st.write(f"Number of Travelers: {num_travelers}")

        # Display additional information based on destination country
        if destination in country_info:
            st.write("Additional Information:")
            st.write(f"- Visa Required: {'Yes' if country_info[destination]['visa_required'] else 'No'}")
            st.write(f"- Electricity Plug Type: {country_info[destination]['plug_type']}")
            st.write(f"- Drinking Water Safety: {country_info[destination]['water_safety']}")
        else:
            st.write("Additional information not available for this destination.")

if __name__ == "__main__":
    main()
