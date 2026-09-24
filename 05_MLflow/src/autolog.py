import mlflow
import mlflow.sklearn
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.datasets import load_wine
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

import dagshub
dagshub.init(repo_owner='mirzanasrullah994', repo_name='MLOps_course_work', mlflow=True)

mlflow.set_tracking_uri("https://dagshub.com/mirzanasrullah994/MLOps_course_work.mlflow")

mlflow.set_experiment("YT-MLOPS-Exp1")
mlflow.autolog()
wine = load_wine()
X = wine.data
y = wine.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

max_depth = 20
n_estimators = 10

with mlflow.start_run():
    rf = RandomForestClassifier(
        max_depth=max_depth,
        n_estimators=n_estimators,
        random_state=42
    )
    rf.fit(X_train, y_train)

    y_pred = rf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)


    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(6, 6))
    sns.heatmap(
        cm,
        annot=True,
        fmt="d",
        cmap="Blues",
        xticklabels=wine.target_names,
        yticklabels=wine.target_names
    )
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title("Confusion Matrix")

    plt.savefig("Confusion-matrix.png")
    plt.close()

    # set tags
    mlflow.set_tags({"Author": "Nasrullah", "Project": "Wine Classification"})

    # log artifacts
    mlflow.log_artifact(__file__)

    print(f"{accuracy:.3f}")