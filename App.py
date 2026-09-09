import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Fahrenheit to Celsius",
    page_icon="🌡️",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
    .main-title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        margin-bottom: 10px;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        color: gray;
        margin-bottom: 30px;
    }

    .result-box {
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        font-size: 25px;
        font-weight: bold;
        margin-top: 25px;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown(
    '<div class="main-title">🌡️ Temperature Converter</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Convert Fahrenheit temperature to Celsius</div>',
    unsafe_allow_html=True
)

# Input section
st.subheader("Enter Temperature")

fahrenheit = st.number_input(
    "🌡️ Temperature in Fahrenheit (°F)",
    value=32.0,
    step=0.1
)

# Calculate button
if st.button("🔄 Convert to Celsius", use_container_width=True):

    celsius = (fahrenheit - 32) * 5 / 9

    st.markdown(
        f"""
        <div class="result-box">
            {fahrenheit:.2f} °F = {celsius:.3f} °C
        </div>
        """,
        unsafe_allow_html=True
    )

    st.success("✅ Conversion completed successfully!")
