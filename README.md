# instagram_spammer_detection

live demo -https://instagramspammerdetection.streamlit.app/
# 📱 Instagram Spammer Detection using Machine Learning

Hi! I'm Priti, and this is a mini ML project where I built a web app to detect **spam comments** on Instagram. Using basic NLP and a classification model, the app classifies any comment as either a **spammer** or **genuine** — all in real time through a simple Streamlit interface!

---

## 🚀 Live Demo

👉 [Try the Live App on Streamlit](https://your-username.streamlit.app](https://instagramspammerdetection.streamlit.app/)  

---

## 💡 About the Project

The goal was to build something that could analyze Instagram-style comments and flag potential spam. This project covers:

- Text preprocessing and vectorization (TF-IDF)
- Training a classifier to differentiate spam vs. real comments
- Building an interactive UI using Streamlit
- Deploying the app live for anyone to test

---

## 🔍 Features

- 🚫 Detects if a comment is spam
- ⚡ Fast real-time predictions
- 🎯 Simple, clean web UI with instant feedback
- 🧠 ML model trained from scratch 

---

## 🧠 Model Details

- **Vectorizer:** TF-IDF
- **Classifier Used:** Logistic Regression 
- **Training Data:** Pre-labeled Instagram comments

---

## 🛠 Tools & Technologies

| Tool         | Purpose                      |
|--------------|------------------------------|
| Python       | Core programming language     |
| Scikit-learn | Machine learning pipeline     |
| Pandas       | Data handling & preprocessing |
| Streamlit    | Web app framework             |
| Joblib       | Saving and loading models     |

---

## 🏁 Getting Started Locally

```bash
# Clone the repository
git clone https://github.com/priti-instagram-spam-detector.git
cd instagram-spammer-detection

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
