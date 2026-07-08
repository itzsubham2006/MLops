import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.datasets import load_wine
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Mention your experiment below

mlflow.set_tracking_uri("http://127.0.0.1:5000")

wine = load_wine()

x = wine.data
y = wine.target

# splitting the dataset into training and test datas

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=2, test_size=0.1)

max_depth = 10
n_estimators = 8
 

mlflow.set_experiment('MLops-Exp1')

with mlflow.start_run():
    
    model = RandomForestClassifier(max_depth=max_depth, n_estimators=n_estimators, random_state=42)
    model.fit(x_train, y_train)
    
    # calculating the accuracy and precision score of the model
    
    y_pred = model.predict(x_test)
    
    accuracy = accuracy_score(y_test, y_pred)
    confusion = confusion_matrix(y_test, y_pred)
   
    mlflow.log_metric('accuracy', accuracy)
    # mlflow.log_metric('confusion', confusion)
    

    mlflow.log_param('max_depth', max_depth)
    mlflow.log_param('n_estimators', n_estimators)
    
    plt.figure(figsize=(6,6))
    sns.heatmap(confusion, annot=True, fmt='d', cmap='Blues', xticklabels=wine.target_names, yticklabels=wine.target_names)
    plt.ylabel('Actual -->')
    plt.xlabel('Predicted -->')
    plt.title('Confusion Matrix')

    plt.savefig('Confusion_matrix.png')

    mlflow.log_artifact("Confusion_matrix.png")
    mlflow.log_artifact(__file__)
    
    mlflow.set_tags(
        
        {"Author": "Subham Pathak", "Project": "Wine Classifications"}
        
        )
    
    mlflow.sklearn.load_model(model, "Random-Forest-model")
    
    print(accuracy)