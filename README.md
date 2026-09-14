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

## 📂 Project Structure
```text
├── data/                  # Raw and processed datasets
├── notebooks/             # Jupyter notebooks for EDA and model training
├── src/
│   ├── train.py           # Model training and optimization script
│   └── app.py             # Inference API (Flask/FastAPI)
├── Dockerfile             # Docker container configuration
├── requirements.txt       # Python dependencies
├── model.joblib           # Trained model artifact (git-ignored)
└── README.md              # Project documentation
```

---

## 💻 Getting Started

### 1. Prerequisites
Ensure you have the following installed:
* Python 3.9+
* Docker
* AWS CLI (configured with appropriate credentials)

### 2. Installation & Local Setup
Clone this repository and install the required dependencies:
```bash
git clone https://github.com/yourusername/mobile-phone-classification.git
cd mobile-phone-classification
pip install -r requirements.txt
```

### 3. Training the Model
Run the training script to evaluate the data and generate the serialized model file:
```bash
python src/train.py
```

---

## ☁️ AWS Deployment Steps

### Step 1: Store Model in Amazon S3
Upload your serialized model to an S3 bucket so your deployment environment can access it securely:
```bash
aws s3 cp model.joblib s3://your-bucket-name/models/model.joblib
```

### Step 2: Containerize the Application
Build your Docker image locally to package the application code and dependencies:
```bash
docker build -t mobile-classifier .
```

### Step 3: Push to Amazon ECR
Authenticate your local Docker client with your AWS registry and push the image:
```bash
# Authenticate ECR
aws ecr get-login-password --region your-region | docker login --username AWS --password-stdin your-account-id.dkr.ecr.your-region.amazonaws.com

# Tag and Push
docker tag mobile-classifier:latest your-account-id.dkr.ecr.your-region.amazonaws.com/mobile-classifier:latest
docker push your-account-id.dkr.ecr.your-region.amazonaws.com/mobile-classifier:latest
```

### Step 4: Deploy and Serve Predictions
1. Create a serverless function via **AWS Lambda** (or a service task on **Amazon ECS**) using your uploaded ECR image.
2. Link an environment variable `MODEL_S3_PATH` pointing to your S3 bucket.
3. Expose the function securely using **Amazon API Gateway** to receive HTTP POST requests.

---

## 🔌 API Usage Example

### Request
`POST https://your-api-gateway-url.amazonaws.com/predict`

**Body (JSON):**
```json
{
  "battery_power": 1043,
  "blue": 1,
  "clock_speed": 1.8,
  "dual_sim": 1,
  "fc": 14,
  "four_g": 1,
  "int_memory": 5,
  "m_dep": 0.1,
  "mobile_wt": 193,
  "n_cores": 3,
  "pc": 16,
  "px_height": 226,
  "px_width": 1412,
  "ram": 3476,
  "sc_h": 12,
  "sc_w": 7,
  "talk_time": 2,
  "three_g": 0,
  "touch_screen": 1,
  "wifi": 0
}
```

### Response
```json
{
  "prediction": 3,
  "price_range": "Very High Cost"
}
```
