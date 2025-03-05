import streamlit as st
import pint

# Pint Unit Registry
ureg = pint.UnitRegistry()

st.title("🔄 Advanced Unit Converter")

# Get all available units dynamically
all_units = list(ureg)  # Pint ke saare units load ho jayenge

# User Input
value = st.number_input("Enter Value:", format="%.4f")

# From Unit & To Unit Dropdowns
from_unit = st.selectbox("From Unit:", all_units)
to_unit = st.selectbox("To Unit:", all_units)

# Convert Button
if st.button("Convert"):
    try:
        result = (value * ureg(from_unit)).to(to_unit)
        st.success(f"✅ {value} {from_unit} = {result}")
    except pint.DimensionalityError:
        st.error("❌ Incompatible units! Cannot convert these.")
    except Exception as e:
        st.error(f"❌ Error: {e}")
