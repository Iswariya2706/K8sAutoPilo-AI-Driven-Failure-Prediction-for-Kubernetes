# K8sAutoPilo
AI-Driven-Failure-Prediction-for-Kubernetes

Overview
K8sAutoPilo is an AI-driven failure prediction system for Kubernetes clusters. It leverages Prometheus for real-time data generation, a Random Forest model trained on historical failure datasets (generated via LitmusChaos), and predictive analytics to proactively identify potential failures.
Key Features
•	Real-time Data Collection: Uses Prometheus to gather Kubernetes cluster metrics.
•	Failure Prediction Model: Trained using historical datasets with Random Forest.
•	Automated Failure Detection: Predicts failures and helps in proactive issue resolution.
•	Seamless Integration: Directly processes Prometheus-generated data and predicts failures.

Tech Stack
•	Kubernetes (for cluster management)
•	Prometheus (for real-time metric collection)
•	LitmusChaos (for generating historical failure datasets)
•	Random Forest Model (for failure prediction)
•	Python, Pandas, Sklearn (for data processing and ML model training)
•	Flask/FastAPI (for API deployment)
•	Tkinter (for visualization)

Project Flow
1.	Kubernetes Cluster Data ➝ Collected using Prometheus.
2.	Data Loading ➝ The collected data is directly fed into the model.
3.	Failure Prediction Model ➝ Trained with LitmusChaos-generated failure datasets using Random Forest.
4.	Prediction Output ➝ Model predicts possible failures.
5.	Result Visualization ➝ Output is displayed using Tkinter or APIs.

 
