import pandas as pd
import pickle
import tkinter as tk
from tkinter import messagebox
from sklearn.preprocessing import LabelEncoder
import time
from datetime import datetime

# Load the trained model
with open(r"C:\Users\satha\Downloads\failure_prediction_model_trained.pkl", "rb") as file:
    model, label_encoder, scaler = pickle.load(file)

# Retrieve the expected feature names from the trained model
try:
    expected_features = model.feature_names_in_  # Works for newer Scikit-learn versions
except AttributeError:
    expected_features = [f"feature_{i}" for i in range(105)]  # Replace with actual feature names if available

# Initialize Tkinter (but keep hidden)
root = tk.Tk()
root.withdraw()  # Hide main window

# Initialize Label Encoders
encoders = {}

# **Continuous Monitoring Loop**
while True:
    try:
        print(f"🔄 Checking for failures at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}...")

        # Load the latest Prometheus log data (assumes file updates periodically)
        df_logs = pd.read_csv(r"C:\Users\satha\Downloads\prometheus_generated_logs.csv")

        # Ensure test dataset has all expected features
        for feature in expected_features:
            if feature not in df_logs.columns:
                df_logs[feature] = 0  # Default value for missing features

        # Encode categorical columns
        for column in df_logs.select_dtypes(include=["object"]).columns:
            if column not in encoders:
                encoders[column] = LabelEncoder()
                df_logs[column] = encoders[column].fit(df_logs[column])  # Fit only once
            else:
                df_logs[column] = encoders[column].transform(df_logs[column])

        # Extract only the necessary features for prediction
        df_features = df_logs[expected_features]

        # Scale the features (apply the same scaling as during training)
        df_features_scaled = scaler.transform(df_features)

        # Make predictions
        df_logs["Failure Prediction"] = model.predict(df_features_scaled)

        # Show more info about predictions if necessary
        print(f"Predictions:\n{df_logs[['Node', 'Failure Prediction']].head()}")

        # Filter failure cases (assuming 1 is failure)
        failures = df_logs[df_logs["Failure Prediction"] == 1]

        # Show alert if failures are detected
        if not failures.empty:
            failure_messages = "\n".join(
                f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Node: {row.get('Node', 'N/A')}, Failure: {row.get('Failure Type', 'Unknown')}"
                for _, row in failures.iterrows()
            )
            messagebox.showwarning("Failure Alert 🚨", f"Predicted Failures:\n{failure_messages}")
        else:
            print("✅ No failures detected. Systems running smoothly.")

    except Exception as e:
        print(f"⚠️ Error in processing: {e}")

    # Wait for 5 seconds before checking again (adjustable)
    time.sleep(5)
