# instagram_spammer_detection

live demo -https://instagramspammerdetection.streamlit.app/
# 📱 Instagram Spammer Detection 🕵️‍♀️

A machine learning project to detect **fake Instagram accounts** using numeric profile features—with a live Streamlit app for real-time testing!

---

## 🚀 Live Demo

Try the real-time app here:  
👉 [instagramspammerdetection.streamlit.app](https://instagramspammerdetection.streamlit.app/)

---

## 🧠 About the Project

This project identifies whether an Instagram profile is **genuine** or **fake** based on structured numeric data (followers, posts, engagement, etc.). It includes:

1. **Exploratory Data Analysis** (EDA)  
2. **Decision Tree classifier** training  
3. **Model evaluation**: accuracy, confusion matrix, feature importance  
4. **A Streamlit UI** for interactive input/output  
5. **Model saving** with `pickle` for deployment

---

## 🧩 Model Details

- **Vectorizer:** N/A (numeric data only)  
- **Classifier:** Decision Tree (`sklearn`)  
- **Saved Model:** `model.pkl` using `pickle`  
- **Evaluation Metrics:** Accuracy, confusion matrix, classification report  
- **Feature Importance:** Visualized via barplot

---

## 🗂 Project Files

| File                                 | Function                                                 |
|--------------------------------------|----------------------------------------------------------|
| `instagram_spammer_detection.ipynb`  | Notebook for EDA and modeling                            |
| `app.py` or similar                  | Streamlit front-end—loads the model and handles input    |
| `model.pkl`                          | Saved ML model                                           |
| `requirements.txt`                   | Python dependencies                                      |
| `train.csv`, `test.csv`             | Labeled datasets for training and evaluation             |

---

## 🛠 Tech Stack

| Tool         | Purpose                                |
|--------------|----------------------------------------|
| Python       | Core language                          |
| Pandas       | Data processing                        |
| Seaborn, Matplotlib | Data visualization              |
| Scikit-learn | Decision Tree model & evaluation       |
| Pickle       | Model persistence                      |
| Streamlit    | Web app interface                      |

---

## ⚙️ Running the Project Locally

```bash
# Clone the repository
git clone https://github.com/priti378/instagram_spammer_detection.git
cd instagram_spammer_detection

# Set up an environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Launch the Jupyter notebook
jupyter notebook instagram_spammer_detection.ipynb

# Launch the Streamlit app
streamlit run app.py
📈 How It Works
App loads model.pkl

User enters profile metrics (followers, posts, etc.)

Model predicts Genuine or Fake immediately

Output displayed with feature interpretation
