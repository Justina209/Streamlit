**Customer Churn Analysis**



**Overview**
This project aims to predict customer churn in a telecommunications company using machine learning classification models. 
The goal is to identify customers who are at risk of leaving the company based on their demographic and usage data. 
The project leverages various classification algorithms, including KNeighborsClassifier, LogisticRegression, RandomForestClassifier, 
SVC, GradientBoostingClassifier, and XGBClassifier, to perform churn prediction. 

Hyperparameter tuning is performed using RandomizedSearchCV to optimize model performance, and the models are evaluated
based on F1-score, accuracy, precision, and recall.

**Table of Contents**
Overview
Project Structure
Requirements
Data
Models
Model Evaluation
Results
Installation
Usage
License
Project Structure
The project follows this directory structure:

bash
Copy code
├── data/                   # Contains the raw and processed datasets

│   ├── raw/                # Raw dataset

│   └── processed/          # Processed data ready for modeling

├── notebooks/              # Jupyter notebooks for data exploration, visualization, and modeling

├── scripts/                # Python scripts for data preprocessing, training, and evaluation

├── models/                 # Trained machine learning models

├── results/                # Model performance metrics and visualizations

├── requirements.txt        # List of dependencies

└── README.md               # Project documentation

**Requirements**
To set up this project, you'll need Python 3.x and the following dependencies:

pandas: Data manipulation

scikit-learn: Machine learning models and tools

imbalanced-learn: For oversampling techniques like SMOTE

xgboost: For the XGBoost classifier

matplotlib and seaborn: For data visualization

numpy: For numerical computations

Install all dependencies by running:


The data is split into a 
training set and test set, 
and preprocessing steps such as feature scaling,
missing data handling, 
and encoding categorical variables are applied before model training.

Models
The following classification models were tested in this project:

KNeighborsClassifier: A simple distance-based algorithm for classification.


LogisticRegression: A linear model for binary classification.

RandomForestClassifier: An ensemble model using multiple decision trees.

SVC (Support Vector Classifier): A classifier based on hyperplanes for classification.

GradientBoostingClassifier: An ensemble technique that builds models sequentially to correct previous errors.

XGBClassifier: A gradient boosting method based on decision trees that performs well with large datasets.

Model Evaluation
Models are evaluated using the following metrics:

Accuracy: Proportion of correctly classified instances.

Precision: Proportion of true positive predictions out of all positive predictions.

Recall: Proportion of true positive predictions out of all actual positives.

F1-score: Harmonic mean of precision and recall, providing a balanced evaluation.

Each model is also tuned using RandomizedSearchCV to optimize hyperparameters and improve performance.



License
This project is licensed under the MIT License. See the LICENSE file for more details.

