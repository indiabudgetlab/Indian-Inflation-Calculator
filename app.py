import pandas as pd
import streamlit as st

# Sample CPI Data (fake numbers for testing)
data = {
    'Year': [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    'Delhi': [110, 115, 120, 125, 130, 135, 140, 150, 160],
    'Mumbai': [112, 117, 121, 127, 132, 137, 143, 152, 161],
    'Chennai': [108, 114, 119, 124, 129, 134, 139, 148, 158],
    'Bangalore': [109, 116, 122, 128, 133, 138, 144, 153, 162]
}

df = pd.DataFrame(data)
df.set_index('Year', inplace=True)

# Inflation calculation function
def adjust_inflation(amount, start_year, end_year, city):
    if start_year not in df.index or end_year not in df.index:
        return "Invalid year selected."
    if city not in df.columns:
        return "City not found."
    start_cpi = df.loc[start_year, city]
    end_cpi = df.loc[end_year, city]
    adjusted_amount = amount * (end_cpi / start_cpi)
    return round(adjusted_amount, 2)

# Streamlit App Interface
st.title("📈 Inflation Calculator for Indian Cities")
st.markdown("See how inflation affects your money between two years in different Indian cities! 💸")

city = st.selectbox("Choose a city", df.columns)
start_year = st.selectbox("Start Year", df.index)
end_year = st.selectbox("End Year", df.index)
amount = st.number_input("Amount in ₹", min_value=0.0)

if st.button("Calculate"):
    result = adjust_inflation(amount, start_year, end_year, city)
    st.success(f"₹{amount} in {start_year} is approximately ₹{result} in {end_year} ({city})")
