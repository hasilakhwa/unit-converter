import streamlit as st
import pint

# CSS fix for dropdown scrolling on mobile
st.markdown(
    """
    <style>
    /* Fix dropdown scrolling issue */
    .stSelectbox div[data-baseweb="select"] {
        max-height: 200px !important;
        overflow-y: auto !important;
    }
    .stSelectbox div[role="listbox"] {
        overflow-y: auto !important;
        max-height: 200px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Unit conversion setup
ureg = pint.UnitRegistry()

st.title("📏 Unit Converter")

# List of units
units = ["meter", "kilometer", "centimeter", "millimeter", "inch", "foot", "yard", "mile", "gram", "kilogram", "pound", "ounce", "liter", "milliliter", "gallon"]

# Dropdowns for unit selection
from_unit = st.selectbox("From Unit:", units)
to_unit = st.selectbox("To Unit:", units)

# Input for value
value = st.number_input("Enter Value:", min_value=0.0, format="%.2f")

# Convert button
if st.button("Convert"):
    try:
        result = (value * ureg(from_unit)).to(to_unit)
        st.success(f"{value} {from_unit} = {result.magnitude:.4f} {to_unit}")
    except pint.errors.DimensionalityError:
        st.error("⚠ Incompatible units! Please choose the correct unit types.")

