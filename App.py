import streamlit as st

st.title("⭕ Circle Area Calculator")

st.write("This application will calculate the area of a circle.")

radius = st.number_input(
    "Please enter the radius of your circle:",
    min_value=0.0,
    value=1.0
)

pi = 3.14
area = pi * (radius ** 2)

st.success(f"Area of your circle is: {area:.5f}")
