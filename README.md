# Weather App

## Introduction

The Weather App is a simple web application built using Streamlit, a Python library for creating interactive web apps. It fetches real-time weather data from the OpenWeatherMap API based on user input and displays it in a user-friendly manner.

## Getting Started

To use the Weather App, you need to obtain an API key from OpenWeatherMap. Unless you create your API key from OpenWeatherMap and paste it into the code, the app won't work.

### Prerequisites

To run the Weather App on your local machine, you need:

- Python installed on your system. You can download and install Python from [here](https://www.python.org/downloads/).
- The Streamlit library. Install it using pip:
```
pip install streamlit
```
### Installation

1. Clone the repository:


2. Navigate to the project directory:


3. Install the required Python packages:


## How It Works

The Weather App allows users to enter a location in the text input field. It then fetches weather data from the OpenWeatherMap API for that location and displays it on the screen. The background image of the app changes dynamically based on the current weather conditions.

### Implementation Details

- The app is built using the Streamlit library, which makes it easy to create interactive web apps with Python.
- It uses the `requests` library to make HTTP requests to the OpenWeatherMap API and fetch weather data.
- Weather data is displayed using Streamlit's UI components such as `st.title()`, `st.subheader()`, and `st.write()`.
- Background images are sourced from Unsplash and displayed using CSS styling.
- A watermark "Developed by Gokul Pathak" is added to the bottom right corner of the app to provide attribution to the developer.

## Usage

To run the Weather App on your local machine, execute the following command:

```
streamlit run app.py
```

This will launch the app in your default web browser, and you can start using it to check the weather for any location.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or feedback, please contact the developer:

Gokul Pathak - [GitHub](https://github.com/gokul-pathak)

