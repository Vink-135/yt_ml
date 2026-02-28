import streamlit as st
import numpy as np
import joblib

model = joblib.load("model.pkl")

st.title("YouTube Video Demand Predictor")

likes = st.number_input("Likes", min_value=0)
comments = st.number_input("Comments", min_value=0)
dislikes = st.number_input("Dislikes", min_value=0)

engagement = (likes + comments - dislikes) / (likes + comments + 1)

if st.button("Predict Demand"):
    prediction = model.predict([[likes, comments, dislikes, engagement]])
    
    if prediction[0] == 1:
        st.success("High Demand Video")
    else:
        st.error("Low Demand Video")



