import streamlit as st
import requests
import json

st.title("Weather App")

# API key
api_key = "Your API key" #confidential

# Default location
default_location = "Baglung, Nepal"

# User input
user_input = st.text_input("Enter location", default_location)

# Function to fetch weather data
def fetch_weather_data(location):
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    response = requests.get(base_url)
    data = response.json()
    return data

# Function to display weather data
def display_weather_data(data):
    try:
        st.subheader(f"Weather in {data['name']}, {data['sys']['country']}")
        st.write(f"Current Temperature: {data['main']['temp']} K / {(data['main']['temp'] - 273.15):.2f}°C / {(data['main']['temp'] * 9/5 - 459.67):.2f}°F")
        st.write(f"Feels Like: {data['main']['feels_like']} K / {(data['main']['feels_like'] - 273.15):.2f}°C / {(data['main']['feels_like'] * 9/5 - 459.67):.2f}°F")
        st.write(f"Humidity: {data['main']['humidity']}%")
        st.write(f"Wind Speed: {data['wind']['speed']} m/s")
        
        weather_description = data['weather'][0]['description']
        st.write(f"Weather Description: {weather_description.capitalize()}")
        
        if 'rain' in data:
            rain_amount = data['rain']['1h']
            st.write(f"Rain Amount: {rain_amount} mm (last hour)")
        
        if 'snow' in data:
            snow_amount = data['snow']['1h']
            st.write(f"Snow Amount: {snow_amount} cm (last hour)")
        
        # Set background image based on weather condition
        set_background(weather_description)

    except KeyError as e:
        st.write("Error: Invalid location or API response. Please check the location and try again.")

def set_background(weather_description):
    # Mapping weather conditions to appropriate image keywords
    weather_images = {
        "clear sky": "sun",
        "few clouds": "clouds",
        "scattered clouds": "clouds",
        "broken clouds": "clouds",
        "overcast clouds": "clouds",
        "light rain": "rain",
        "moderate rain": "rain",
        "heavy intensity rain": "rain",
        "light snow": "snow",
        "moderate snow": "snow",
        "heavy snow": "snow"
    }

    # Selecting a random image from Unsplash based on weather condition
    image_keyword = weather_images.get(weather_description.lower(), "weather")
    image_url = f"https://source.unsplash.com/featured/?{image_keyword}"
    st.markdown(f'<style>.stApp {{background-image: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), url({image_url}); background-size: cover;}}</style>', unsafe_allow_html=True)

    # Add watermark
    st.markdown(f'<style>.stApp:after {{content: "Developed by Gokul Pathak"; position: fixed; bottom: 20px; right: 20px; color: white; font-size: 16px; opacity: 0.7;}}</style>', unsafe_allow_html=True)

weather_data = fetch_weather_data(user_input)
display_weather_data(weather_data)
