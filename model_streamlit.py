import streamlit as st
import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the pickled model
with open("Fake_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)
# Streamlit App
st.title("News Classification App")
st.write("Enter a news article and classify it using the trained model.")

# User input
news_text = st.text_area("Enter news content:", "")

if st.button("Predict"):
    if news_text.strip() == "":
        st.warning("Please enter some news content.")
    else:
        # Convert input into a DataFrame
        input_df = pd.DataFrame([news_text], columns=["news_text"])
        
        # Transform using TF-IDF
        # transformed_text = vectorizer.transform(input_df["news_text"])
        
        # Predict using the model
        prediction = model.predict(input_df["news_text"])
        
        # Display result
        #st.success(f"Prediction: {prediction}")
        if prediction == 1:
            st.success("The news is likely to be real.")
        else:
            st.error("The news is likely to be fake.")
# Run the app using the command: streamlit run Fake_streamlit.py
