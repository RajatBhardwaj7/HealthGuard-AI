from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
import os

from backend.database import (
    create_tables,
    create_user,
    user_exists,
    login_user,
    save_prediction,
    get_prediction_history
)

from backend.auth import (
    hash_password,
    verify_password
)


app = Flask(__name__)
CORS(app)


# ===========================================
# Load ML Model
# ===========================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "diabetes_model.pkl"
)

SCALER_PATH = os.path.join(
    BASE_DIR,
    "models",
    "scaler.pkl"
)


model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)


# Create database tables
create_tables()



# ===========================================
# Home API
# ===========================================

@app.route("/")
def home():
    return "HealthGuard-AI Backend Running"



# ===========================================
# Register API
# ===========================================

@app.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")


    if not name or not email or not password:
        return jsonify({
            "message": "All fields are required."
        }), 400


    if user_exists(email):
        return jsonify({
            "message": "Email already registered."
        }), 400


    hashed_password = hash_password(password)


    create_user(
        name,
        email,
        hashed_password
    )


    return jsonify({
        "message": "Account created successfully."
    }), 201



# ===========================================
# Login API
# ===========================================

@app.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    email = data.get("email")
    password = data.get("password")


    user = login_user(email)


    if user is None:
        return jsonify({
            "message": "Invalid email or password."
        }), 401


    if not verify_password(password, user["password"]):
        return jsonify({
            "message": "Invalid email or password."
        }), 401


    return jsonify({
        "message": "Login Successful",
        "user": {
            "id": user["id"],
            "name": user["name"],
            "email": user["email"]
        }
    })



# ===========================================
# Prediction API
# ===========================================

@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()


    features = np.array([[
        data["Pregnancies"],
        data["Glucose"],
        data["BloodPressure"],
        data["SkinThickness"],
        data["Insulin"],
        data["BMI"],
        data["DiabetesPedigreeFunction"],
        data["Age"]
    ]])


    features = scaler.transform(features)


    prediction = model.predict(features)[0]


    probability = model.predict_proba(features)[0][1]


    result = "Diabetic" if prediction == 1 else "Not Diabetic"



    save_prediction(
        data["user_email"],
        data["Pregnancies"],
        data["Glucose"],
        data["BloodPressure"],
        data["SkinThickness"],
        data["Insulin"],
        data["BMI"],
        data["DiabetesPedigreeFunction"],
        data["Age"],
        result,
        round(probability * 100, 2)
    )


    return jsonify({
        "prediction": result,
        "probability": round(probability * 100, 2)
    })



# ===========================================
# Prediction History API
# ===========================================

@app.route("/history", methods=["POST"])
def history():

    data = request.get_json()


    history = get_prediction_history(
        data["user_email"]
    )


    history_list = []


    for row in history:

        history_list.append({

            "prediction": row["prediction"],
            "probability": row["probability"],
            "glucose": row["glucose"],
            "bmi": row["bmi"],
            "age": row["age"],
            "date": row["created_at"]

        })


    return jsonify(history_list)



# ===========================================
# Run Application
# ===========================================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5001)),
        debug=False
    )