import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import os

# Load dataset
data = pd.read_csv("crop_recommendation.csv")

# Features
X = data.drop("label", axis=1)

# Target
y = data["label"]

# Label Encoding
encoder = LabelEncoder()
y = encoder.fit_transform(y)

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Random Forest Model
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

# Prediction
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("Accuracy:", accuracy)

# Create model folder
os.makedirs("model", exist_ok=True)

# Save model
joblib.dump(model, "model/crop_model.pkl")

# Save encoder
joblib.dump(encoder, "model/label_encoder.pkl")

print("Model Saved Successfully!")