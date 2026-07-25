from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np

from database import (
    create_tables,
    create_user,
    user_exists,
    login_user
)

from auth import (
    hash_password,
    verify_password
)

app = Flask(__name__)
CORS(app)

# -----------------------------
# Load ML Model
# -----------------------------
model = joblib.load("../models/diabetes_model.pkl")
scaler = joblib.load("../models/scaler.pkl")

# Create database tables
create_tables()


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

    return jsonify({
        "prediction": result,
        "probability": round(probability * 100, 2)
    })


if __name__ == "__main__":
    app.run(debug=True)