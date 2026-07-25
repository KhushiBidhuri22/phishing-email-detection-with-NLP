#  AI-Driven Phishing Email Detection Using NLP

An end-to-end Machine Learning project that detects phishing emails using Natural Language Processing (NLP) techniques. The project preprocesses email text, extracts features using TF-IDF, trains multiple machine learning models, and compares their performance to accurately classify emails as **Phishing** or **Legitimate**.

---

##  Project Overview

Phishing attacks are one of the most common forms of cybercrime, where attackers trick users into revealing sensitive information through fraudulent emails.

This project aims to build an intelligent phishing email detection system using NLP and Machine Learning to automatically identify phishing emails with high accuracy.

---

##  Features

- Data preprocessing and text cleaning
- Exploratory Data Analysis (EDA)
- TF-IDF feature extraction
- Training multiple ML models
- Performance comparison
- Model evaluation using various metrics
- Confusion Matrix visualization
- Ready for Flask deployment

---

##  Dataset

The dataset used for this project is publicly available on Kaggle.

**Dataset Link:**

https://www.kaggle.com/datasets/naserabdullahalam/phishing-email-dataset

> **Note:** The dataset is not included in this repository because it exceeds GitHub's file size limit.

After downloading, place the dataset inside your project folder.

---

##  Technologies Used

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- NLTK
- Joblib

---

##  Workflow

1. Import Dataset
2. Data Cleaning
3. Text Preprocessing
4. Exploratory Data Analysis
5. Feature Extraction using TF-IDF
6. Train-Test Split
7. Model Training
8. Model Evaluation
9. Model Comparison
10. Save Best Model
11. Flask Deployment (Future Scope)

---

##  Machine Learning Models Used

- Logistic Regression
- Multinomial Naive Bayes
- Random Forest Classifier

The models were compared using:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

---

##  Evaluation Metrics

The models are evaluated using:

- Accuracy Score
- Precision
- Recall
- F1 Score
- Classification Report
- Confusion Matrix

---

##  Project Structure

```
Phishing-Email-Detection/
│
├── final project.ipynb
├── phishing email detection.ipynb
├── README.md
├── requirements.txt
├── .gitignore
└── data/
```



##  Results

The trained models successfully classified phishing and legitimate emails with high performance.

Model performance was evaluated using multiple classification metrics, and the best-performing model was selected based on overall accuracy and F1-score.

---



