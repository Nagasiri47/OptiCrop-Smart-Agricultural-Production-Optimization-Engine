from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

# Load model and label encoder
model = joblib.load("model/crop_model.pkl")
encoder = joblib.load("model/label_encoder.pkl")


# ==========================
# HOME PAGE
# ==========================
@app.route("/")
def home():
    return render_template("index.html")


# ==========================
# SCENARIO 1
# Crop Recommendation
# ==========================
@app.route("/predict", methods=["POST"])
def predict():

    N = float(request.form["N"])
    P = float(request.form["P"])
    K = float(request.form["K"])
    temperature = float(request.form["temperature"])
    humidity = float(request.form["humidity"])
    ph = float(request.form["ph"])
    rainfall = float(request.form["rainfall"])

    data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])

    prediction = model.predict(data)

    crop = encoder.inverse_transform(prediction)[0]

    return render_template("result.html", prediction=crop)


# ==========================
# SCENARIO 2 PAGE
# ==========================
@app.route("/suitability")
def suitability():
    return render_template("suitability.html")


# ==========================
# SCENARIO 2
# Crop Suitability
# ==========================
@app.route("/check_suitability", methods=["POST"])
def check_suitability():

    crop = request.form["crop"]
    temperature = float(request.form["temperature"])
    humidity = float(request.form["humidity"])
    ph = float(request.form["ph"])
    rainfall = float(request.form["rainfall"])

    crop_ranges = {

        "rice": {
            "temperature": (20, 30),
            "humidity": (80, 90),
            "ph": (5.5, 7.0),
            "rainfall": (150, 300)
        },

        "maize": {
            "temperature": (18, 35),
            "humidity": (50, 80),
            "ph": (5.5, 7.5),
            "rainfall": (50, 150)
        },

        "cotton": {
            "temperature": (21, 35),
            "humidity": (50, 70),
            "ph": (5.8, 8.0),
            "rainfall": (60, 120)
        },

        "wheat": {
            "temperature": (10, 25),
            "humidity": (50, 70),
            "ph": (6.0, 7.5),
            "rainfall": (50, 100)
        }

    }

    if crop not in crop_ranges:
        result = "Crop data not available."
    else:
        data = crop_ranges[crop]

        if (
            data["temperature"][0] <= temperature <= data["temperature"][1]
             and data["humidity"][0] <= humidity <= data["humidity"][1]
            and  data["ph"][0] <= ph <= data["ph"][1]
            and data["rainfall"][0] <= rainfall <= data["rainfall"][1]
        ):
            result = "Suitable ✅"
        else:
            result = "Not Suitable ❌"

    return render_template("result.html", prediction=result)


# ==========================
# SCENARIO 3
# Research Dashboard
# ==========================
@app.route("/research")
def research():
    return render_template("research.html")


# ==========================
# RUN APPLICATION
# ==========================
if __name__ == "__main__":
    app.run(debug=True)