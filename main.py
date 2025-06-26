import pickle
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from os import path

st.title("🍺 Beer Servings Estimation App")

# Load the model
file_name = "model.pkl"
with open(path.join("model", file_name), "rb") as f:
    lr_model = pickle.load(f)

# Input from user
country = st.selectbox(
    "Select a country",
    ["Germany", "USA", "India", "Brazil", "Czech Republic", "Ireland", "Japan"],
)

continent = st.selectbox(
    "Select a continent",
    ["Europe", "North America", "Asia", "South America", "Africa", "Oceania"],
)

beer = st.number_input("🍺 Beer servings", min_value=0)
spirit = st.number_input("🥃 Spirit servings", min_value=0)
wine = st.number_input("🍷 Wine servings", min_value=0)

# Encoding continent (example label encoding)
continent_dict = {
    "Africa": 0,
    "Asia": 1,
    "Europe": 2,
    "North America": 3,
    "Oceania": 4,
    "South America": 5
 }
# continent_encoded = continent_dict[continent]

# Prepare input for model
input_data = np.array([[beer, spirit, wine]])

# Prediction and chart
if st.button("🔍 Predict Alcohol Consumption"):
    prediction = lr_model.predict(input_data)
    st.success(f"Estimated Total Litres of Pure Alcohol: **{prediction[0]:.2f} litres**")

    # Create bar chart of inputs
    st.subheader("🍹 Drink Servings Breakdown")
    fig, ax = plt.subplots()
    drinks = ['Beer', 'Spirit', 'Wine']
    servings = [beer, spirit, wine]
    bars = ax.bar(drinks, servings, color=["#f4a261", "#e76f51", "#2a9d8f"])

    # Annotate bars
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2.0, yval + 1, int(yval), ha='center', va='bottom')

    ax.set_ylabel("Servings")
    ax.set_title("User-Entered Beverage Servings")
    st.pyplot(fig)
