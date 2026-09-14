# Mobile Phone Price Classification & AWS Deployment

An end-to-end Machine Learning project that classifies mobile phone price ranges based on their features. The pipeline includes data preprocessing, custom model training using a Kaggle dataset, cloud storage, and deployment into a production environment using AWS.

## 🚀 Project Overview
* **Objective:** Classify mobile phones into 4 distinct price ranges (0: Low Cost, 1: Medium Cost, 2: High Cost, 3: Very High Cost).
* **Dataset:** [Kaggle Mobile Price Classification Dataset](https://www.kaggle.com/datasets/iabhishekofficial/mobile-phone-price-prediction)
* **Tech Stack:** Python, Pandas, Scikit-Learn, Joblib, Docker, AWS (S3, ECR, Lambda/ECS, API Gateway)

---

## 🛠️ Architecture Pipeline

1. **Data & Modeling:** Preprocess data and train a classification model (e.g., Random Forest/XGBoost) locally or via Jupyter Notebook.
2. **Artifact Serialization:** Save the trained model artifact using `joblib`.
3. **Cloud Storage:** Upload the model artifact to an **Amazon S3** bucket.
4. **Containerization:** Package the inference API script (Flask/FastAPI) and dependencies into a **Docker** image.
5. **Deployment:** Push the container image to **Amazon ECR** and deploy it to production via **AWS Lambda** or **Amazon ECS** behind an **API Gateway**.

---
