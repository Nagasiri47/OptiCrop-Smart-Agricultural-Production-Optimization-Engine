import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read dataset
data = pd.read_csv("crop_recommendation.csv")

# ----------------------------
# Crop Distribution
# ----------------------------
plt.figure(figsize=(12,6))
data["label"].value_counts().plot(kind="bar")
plt.title("Crop Distribution")
plt.tight_layout()
plt.savefig("static/images/crop_distribution.png")
plt.close()

# ----------------------------
# Average Temperature
# ----------------------------
plt.figure(figsize=(12,6))
sns.barplot(data=data, x="label", y="temperature")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("static/images/temperature.png")
plt.close()

# ----------------------------
# Average Rainfall
# ----------------------------
plt.figure(figsize=(12,6))
sns.barplot(data=data, x="label", y="rainfall")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("static/images/rainfall.png")
plt.close()

# ----------------------------
# Heatmap
# ----------------------------
plt.figure(figsize=(10,8))
sns.heatmap(data.corr(numeric_only=True), annot=True)
plt.tight_layout()
plt.savefig("static/images/heatmap.png")
plt.close()

print("Graphs Generated Successfully!")