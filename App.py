import streamlit as st

st.title("🌡️ Fahrenheit to Celsius Converter")

st.write("This application will convert temperature from Fahrenheit to Celsius.")

fahrenheit = st.number_input(
    "Enter the temperature in Fahrenheit:",
    value=32.0
)

celsius = (fahrenheit - 32) * 5 / 9

st.success(f"Temperature in Celsius is: {celsius:.3f} °C")