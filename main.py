import pickle
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import os

st.title("🍺 Beer Servings Estimation App")

# Load the model (must be in the same folder)
if not os.path.exists("model.pkl"):
    st.error("❌ 'model.pkl' not found. Please make sure it's in the same folder as this app.")
    st.stop()

with open("model/model.pkl", "rb") as f:

    lr_model = pickle.load(f)

# User Inputs
country = st.selectbox("Select a country", ["Germany", "USA", "India", "Brazil", "Czech Republic", "Ireland", "Japan"])
continent = st.selectbox("Select a continent", ["Europe", "North America", "Asia", "South America", "Africa", "Oceania"])

beer = st.number_input("🍺 Beer servings", min_value=0)
spirit = st.number_input("🥃 Spirit servings", min_value=0)
wine = st.number_input("🍷 Wine servings", min_value=0)

# Encode continent as a number (simple label encoding)
continent_dict = {
    "Africa": 0,
    "Asia": 1,
    "Europe": 2,
    "North America": 3,
    "Oceania": 4,
    "South America": 5
}
continent_encoded = continent_dict[continent]

# Prepare input data for prediction
input_data = np.array([[beer, spirit, wine, continent_encoded]])

# Predict and show result
if st.button("Predict Alcohol Consumption"):
    prediction = lr_model.predict(input_data)
    st.success(f"Estimated Total Litres of Pure Alcohol: **{prediction[0]:.2f} litres**")

    # Plot a bar chart of servings
    st.subheader("🍹 Your Drink Servings")
    fig, ax = plt.subplots()
    drinks = ["Beer", "Spirit", "Wine"]
    servings = [beer, spirit, wine]
    ax.bar(drinks, servings, color=["#f4a261", "#e76f51", "#2a9d8f"])
    ax.set_ylabel("Servings")
    ax.set_title("Beverage Servings Input")
    st.pyplot(fig)
