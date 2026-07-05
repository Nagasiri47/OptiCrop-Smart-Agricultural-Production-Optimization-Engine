# 🌱 OptiCrop – Smart Agricultural Production Optimization Engine

## 📌 Project Overview

OptiCrop is a Machine Learning-based web application that helps farmers choose the most suitable crop based on soil and environmental conditions. The system predicts the best crop using agricultural data such as Nitrogen (N), Phosphorus (P), Potassium (K), temperature, humidity, pH, and rainfall.

The project aims to improve agricultural productivity by providing intelligent crop recommendations and visual insights.

---

## 🎯 Objectives

- Recommend the most suitable crop using Machine Learning.
- Improve agricultural productivity.
- Reduce crop selection errors.
- Provide data visualization for agricultural analysis.
- Create an easy-to-use web application for farmers and researchers.

---

## ✨ Features

- 🌾 Smart Crop Recommendation
- 🤖 Machine Learning Prediction
- 🌡 Temperature Analysis
- 🌧 Rainfall Analysis
- 🧪 Soil Nutrient Analysis (N, P, K)
- 📊 Data Visualization
- 📈 Heatmap Generation
- 🌱 Crop Distribution Graph
- 💻 User-Friendly Flask Web Interface

---

## 🛠 Technologies Used

### Programming Language
- Python 3

### Machine Learning
- Scikit-learn
- Pandas
- NumPy

### Data Visualization
- Matplotlib
- Seaborn

### Web Framework
- Flask

### Frontend
- HTML
- CSS

---

## 📂 Project Structure

```
OptiCrop/
│
├── app.py
├── train_model.py
├── visualization.py
├── crop_recommendation.csv
│
├── model/
│   ├── crop_model.pkl
│   └── label_encoder.pkl
│
├── templates/
│   ├── index.html
│   ├── result.html
│   ├── research.html
│   └── suitability.html
│
├── static/
│   └── images/
│       ├── crop_distribution.png
│       ├── heatmap.png
│       ├── rainfall.png
│       └── temperature.png
│
└── README.md
```

---

## 📊 Input Parameters

The prediction model uses:

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- Soil pH
- Rainfall

---

## 🧠 Machine Learning Model

The crop recommendation model is trained using agricultural datasets.

### Workflow

1. Load Dataset
2. Data Preprocessing
3. Train Machine Learning Model
4. Save Model (.pkl)
5. Load Model in Flask
6. Predict Best Crop
7. Display Result

---

## 📈 Visualizations

The project generates:

- Crop Distribution
- Heatmap
- Temperature Analysis
- Rainfall Analysis

These visualizations help understand agricultural trends and dataset characteristics.

---

## 🚀 How to Run the Project

### Step 1

Clone the repository

```bash
git clone https://github.com/Nagasiri47/OptiCrop-Smart-Agricultural-Production-Optimization-Engine.git
```

### Step 2

Navigate to the project folder

```bash
cd OptiCrop-Smart-Agricultural-Production-Optimization-Engine
```

### Step 3

Install dependencies

```bash
pip install flask pandas numpy matplotlib seaborn scikit-learn joblib
```

### Step 4

Run the application

```bash
python app.py
```

### Step 5

Open your browser

```
http://127.0.0.1:5000
```

---

## 📷 Project Screens

- Home Page
- Crop Recommendation Page
- Result Page
- Research Dashboard
- Suitability Analysis

---

## 🎓 Applications

- Smart Farming
- Precision Agriculture
- Crop Planning
- Agricultural Research
- Farmer Decision Support System

---

## 🔮 Future Enhancements

- AI Chatbot for Farmers
- Disease Detection
- Fertilizer Recommendation
- Weather Forecast Integration
- Multi-language Support
- Mobile Application
- IoT Sensor Integration
- GPS-based Crop Recommendation

---

## 👨‍💻 Author

**Tadisetti Nagasiri**

GitHub:
https://github.com/Nagasiri47

LinkedIn:
(Add your LinkedIn profile link)

---

## ⭐ Support

If you like this project,

⭐ Star this repository

and feel free to contribute.

---

## 📜 License

This project is developed for educational and research purposes.