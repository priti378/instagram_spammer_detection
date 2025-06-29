import streamlit as st
import pickle
import pandas as pd

# Load model and features
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("features.pkl", "rb") as f:
    features = pickle.load(f)

st.title("📱 Instagram Fake Account Detector")

st.markdown("Enter profile features to predict if the account is **Fake** or **Genuine**.")

# Create input fields dynamically
user_input = {}
for feature in features:
    if "length" in feature or "count" in feature or "#" in feature or "words" in feature:
        val = st.number_input(f"{feature}", min_value=0.0, value=0.0, step=1.0)
    else:
        val = st.selectbox(f"{feature}", [0, 1], format_func=lambda x: "Yes (1)" if x == 1 else "No (0)")
    user_input[feature] = val

# Predict button
if st.button("Predict"):
    input_df = pd.DataFrame([user_input])
    pred = model.predict(input_df)[0]
    label = "🚨 FAKE Account" if pred == 1 else "✅ Genuine Account"
    st.subheader(f"Prediction: {label}")



