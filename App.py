import streamlit as st

st.header("Circle Area Calculator")

radius = st.number_input("Enter radius:", min_value=0.0)

if st.button("Calculate Area"):
    pi = 3.14
    area = pi * radius * radius

    st.write("Area of your circle is:", area)
    st.write("Area of your circle is: %.5f" % area)
