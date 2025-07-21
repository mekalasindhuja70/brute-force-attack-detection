# Brute Force Attack Detection 🔐

This project is a machine learning-based web application that detects **Brute Force Attacks** using network traffic data. Built using **Flask**, this app uses a trained ML model to predict whether given input data is malicious or safe.

## 🚀 Features

- Real-time web interface for prediction
- Machine Learning model trained on **CICIDS2017** dataset
- Detects brute force attacks based on 4 key features
- Scalable and extendable system

## 📊 Features Used

The model was trained using the following features:

1. `Destination Port`
2. `Flow Duration`
3. `Total Fwd Packets`
4. `Fwd Packet Length Mean`

## 🧠 ML Model Info

- Model: Support Vector Machine (SVM)
- Trained using preprocessed CICIDS2017 data
- Scaled with StandardScaler (for real-time prediction)

## 🛠️ Tech Stack

- Python 3
- Flask (Web framework)
- Scikit-learn (ML model)
- HTML, CSS (Frontend)
- Git & GitHub (Version control)

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/mekalasindhuja70/brute-force-attack-detection.git
cd brute-force-attack-detection
