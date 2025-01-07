import streamlit as st
import plotly.express as px
from backend import get_data
import math

# Add title, text input, slider, selectbox, and subheader
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    try:
        # Get the temperature/sky data
        filtered_data = get_data(place, days)

        if option == "Temperature":
            temperatures = [dict["main"]["temp"] / 10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            # Create a temperature plot
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)



        if option == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]

            # Divide the image paths into chunks of 5
            chunk_size = 5
            rows = [image_paths[i:i + chunk_size] for i in range(0, len(image_paths), chunk_size)]

            for row in rows:
                cols = st.columns(len(row))  # Create columns dynamically for the current row
                for col, image_path in zip(cols, row):
                    with col:
                        st.image(image_path, width=115)
    except KeyError:
        st.write("Entered Place does not exist!")