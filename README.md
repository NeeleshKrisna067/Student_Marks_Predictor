# 🎓 Student Marks Predictor

A modern web application built with **Streamlit** and **Scikit-Learn** that predicts student exam marks based on study hours, sleep hours, and attendance percentage.

---

## 🚀 Features
- **Accurate Predictions:** Uses a Linear Regression model trained on student data.
- **Interactive UI:** Built with Streamlit for a smooth and responsive user experience.
- **Visual Insights:** Includes data visualization for better understanding of features.
- **Real-time Results:** Get predicted scores instantly based on your specific inputs.

---

## 🏗️ Project Structure
```text
.
├── .venv/               # Virtual environment folder
├── app.py               # Main Streamlit web application
├── main.py              # Model training and evaluation script
├── student_data.csv     # Dataset for training the model
├── model.pkl            # Trained and serialized machine learning model
└── requirements.txt     # List of project dependencies
```

---

## 🛠️ Setup & Installation

### 1. Create a Virtual Environment (Optional but Recommended)
If you don't have one already, create and activate a virtual environment:
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Install Dependencies
Install all the required Python packages:
```powershell
pip install -r requirements.txt
```

### 3. Train the Model
Run the training script to generate the `model.pkl` file:
```powershell
python main.py
```

---

## 🖥️ Running the Web App

To launch the interactive dashboard, run the following command in your terminal:

```powershell
streamlit run app.py
```

*Note: If your environment is not activated, use:*
```powershell
.\.venv\Scripts\python.exe -m streamlit run app.py
```

Once the server starts, open your browser and navigate to **`http://localhost:8501`**.

---

## 📊 Dataset Detail
The model is trained on `student_data.csv` which contains:
- **Study Hours:** Number of hours spent studying daily.
- **Sleep Hours:** Number of hours spent sleeping daily.
- **Attendance:** Percentage of attendance in classes.
- **Marks:** The final marks obtained (Target feature).

---

## ✨ Developed with
- [Python 3.14+](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Scikit-Learn](https://scikit-learn.org/)
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/)
