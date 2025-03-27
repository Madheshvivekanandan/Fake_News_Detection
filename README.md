# Fake News Detection Project

## Overview
This project aims to classify news articles as **real** or **fake** using a **Logistic Regression model** trained on a dataset from Kaggle. The model was trained after preprocessing the dataset and vectorizing the text using **TF-IDF**. A **Streamlit web app** was developed to allow users to input news content and get real-time predictions.

## Dataset
The dataset used for this project was obtained from Kaggle:  
[Fake News Detection Dataset](https://www.kaggle.com/datasets/jainpooja/fake-news-detection/data?select=True.csv)

### Dataset Features:
- **Text**: The news article content  
- **Label**: Indicates whether the news is fake (1) or real (0)  

## Tech Stack
- **Python**  
- **Scikit-learn** (Machine Learning)  
- **Pandas, NumPy** (Data Processing)  
- **Streamlit** (Web App Deployment)  
- **Pickle** (Model Saving & Loading)  

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/fake-news-detection.git
   cd fake-news-detection
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```sh
   streamlit run app.py
   ```
### Model Training 
1. Preprocessing
   -  Removed special characters, punctuation, and stopwords.
   -  Converted text to lowercase.
   -  Applied TF-IDF vectorization.
2. Training:
   - Used Logistic Regression for binary classification.
   - Evaluated using accuracy_score.
3. Saving the Model:
   - Trained model and vectorizer were saved using pickle.
### Streamlit Web App
   - Users can input a news article.
   - The app processes the text, applies TF-IDF, and predicts if the news is real or fake.
   - Displays the prediction result in real time.
## Usage
   - Run the app and enter a news article in the text area.
   - Click Predict to see if the news is Real or Fake.
## Author
Madhesh Vivekanandan
