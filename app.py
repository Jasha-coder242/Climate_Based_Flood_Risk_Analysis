import streamlit as st
import pandas as pd
from data_processing import load_data, preprocess_data
from model_training import train_model, predict
from visualization import plot_results

# Set up the Streamlit app
st.title("Flood Risk Analysis and Prediction")

# Load and preprocess data
data = load_data("data/India_Flood_Inventory_v3.csv")
processed_data = preprocess_data(data)

# Sidebar for user input
st.sidebar.header("User Input")
selected_feature = st.sidebar.selectbox("Select Feature for Prediction", processed_data.columns)

# Train model
if st.sidebar.button("Train Model"):
    model = train_model(processed_data)
    st.success("Model trained successfully!")

# Prediction
if st.sidebar.button("Make Prediction"):
    prediction = predict(model, selected_feature)
    st.write(f"Predicted Risk Level: {prediction}")

# Visualization
st.header("Results Visualization")
if st.button("Show Results"):
    plot_results(processed_data)