# 🩺 HealthGuard-AI

An AI-powered web application that predicts the risk of diabetes using Machine Learning. The application provides real-time predictions, confidence scores, health recommendations, and a secure user authentication system.

---

# 📌 Features

- 🔐 User Registration & Login
- 🤖 Machine Learning Diabetes Prediction
- 📊 Prediction Confidence Score
- 💡 Personalized Health Recommendations
- 🗄️ SQLite Database Integration
- 🔒 Secure Password Hashing
- 🌐 Flask REST API
- 💻 Responsive User Interface
- ⚡ Real-time Predictions
- 📈 Prediction History Tracking

---

# 🚀 Demo

Coming Soon...

---

# 📸 Screenshots

## Login Page

<img src="frontend/images/login.png" width="700">

## Prediction Dashboard

<img src="frontend/images/dashboard.png" width="700">

## Prediction Result

<img src="frontend/images/result.png" width="700">

> *(Replace these images with actual screenshots after uploading them.)*

---

# 🏗️ Project Structure

```text
HealthGuard-AI
│
├── backend/
│   ├── app.py
│   ├── auth.py
│   ├── database.py
│   ├── Procfile
│
├── frontend/
│   ├── css/
│   ├── js/
│   ├── pages/
│   └── index.html
│
├── models/
│   ├── diabetes_model.pkl
│   └── scaler.pkl
│
├── database/
│   └── healthguard.db
│
├── data/
│
├── notebooks/
│
├── reports/
│
├── requirements.txt
│
└── README.md
```

---

# ⚙️ Tech Stack

## Frontend

- HTML5
- CSS3
- JavaScript

## Backend

- Python
- Flask
- Flask REST API
- Flask-CORS

## Machine Learning

- Scikit-Learn
- NumPy
- Pandas
- Joblib

## Database

- SQLite

## Deployment

- Gunicorn
- Render
- Vercel

---

# 🧠 Machine Learning Model

The application uses a trained Machine Learning classification model to predict diabetes risk.

### Input Features

The model takes the following health parameters:

- Pregnancies
- Glucose Level
- Blood Pressure
- Skin Thickness
- Insulin Level
- BMI
- Diabetes Pedigree Function
- Age

### Output

The model provides:

- Prediction result:

  - Diabetic
  - Not Diabetic
- Confidence probability score

---

# 🔐 Authentication System

HealthGuard-AI includes a secure authentication system:

Features:

- User registration
- Login functionality
- Password hashing
- User-specific prediction history

---

# 📊 Prediction Workflow

```
User Input
     |
     ↓
Frontend Interface
     |
     ↓
Flask REST API
     |
     ↓
Data Preprocessing
     |
     ↓
Machine Learning Model
     |
     ↓
Prediction + Confidence Score
     |
     ↓
Store Result in Database
```

---

# 🛠️ Installation & Setup

## 1. Clone Repository

```bash
git clone https://github.com/RajatBhardwaj7/HealthGuard-AI.git
```

Move into the project:

```bash
cd HealthGuard-AI
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

### Mac/Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Run Backend

Navigate to backend:

```bash
cd backend
```

Start Flask server:

```bash
python app.py
```

Backend will run on:

```
http://127.0.0.1:5001
```

---

# 🔌 API Endpoints

## Home

```
GET /
```

Response:

```
HealthGuard-AI Backend Running
```

---

## Register User

```
POST /register
```

Example:

```json
{
"name":"Rajat",
"email":"example@gmail.com",
"password":"password123"
}
```

---

## Login

```
POST /login
```

---

## Predict Diabetes Risk

```
POST /predict
```

Example input:

```json
{
"Pregnancies":6,
"Glucose":148,
"BloodPressure":72,
"SkinThickness":35,
"Insulin":0,
"BMI":33.6,
"DiabetesPedigreeFunction":0.627,
"Age":50,
"user_email":"example@gmail.com"
}
```

Response:

```json
{
"prediction":"Diabetic",
"probability":72.5
}
```

---

## Prediction History

```
POST /history
```

Returns previous predictions of the user.

---

# 📈 Future Improvements

- 🌐 Cloud deployment
- 📱 Mobile application
- 🧬 More disease prediction models
- 📊 Advanced health analytics dashboard
- 🤖 AI health assistant integration
- 📄 Medical report generation

---

# 👨‍💻 Author

**Rajat Bhardwaj**

AI/ML Student | Full Stack ML Developer

GitHub:
https://github.com/RajatBhardwaj7

---

# ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub.
