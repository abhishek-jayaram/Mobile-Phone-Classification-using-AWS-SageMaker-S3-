
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, precision_score, recall_score, f1_score
import sklearn
import joblib
import os
import numpy as np
import pandas as pd
import boto3
import pathlib
from io import StringIO
import argparse


def model_fn(model_dir):
    clf = joblib.load(os.path.join(model_dir, "model.joblib"))
    return clf

if __name__ == "__main__":

    print("[INFO] Reading training data")
    parser = argparse.ArgumentParser()
    parser.add_argument("--n_estimators", type=int, default=100)
    parser.add_argument("--random_state", type=int, default=0)

    parser.add_argument("--model-dir", type=str, default=os.environ.get("SM_MODEL_DIR"))
    parser.add_argument("--train", type=str, default=os.environ.get("SM_CHANNEL_TRAIN"))
    parser.add_argument("--test", type=str, default=os.environ.get("SM_CHANNEL_TEST"))
    parser.add_argument("--train-file", type=str, default="train-V-1.csv")
    parser.add_argument("--test-file", type=str, default="test-V-1.csv")

    args = parser.parse_known_args()

    print("SKLearn Version: ", sklearn.__version__)
    print("Joblib Version: ", joblib.__version__)
    print("[INFO] Reading training data")
    print()
    train_df = pd.read_csv(os.path.join(args[0].train, args[0].train_file))
    test_df = pd.read_csv(os.path.join(args[0].test, args[0].test_file))

    features = list(train_df.columns)
    label = features.pop(-1)

    print("Building training and testing datasets")
    print()
    X_train = train_df[features]
    X_test = test_df[features]
    y_train = train_df[label]
    y_test = test_df[label]

    print('Colum order:')
    print(features)
    print()


    print("Label column: ", label)
    print()

    print("Data Shape:")
    print()
    print("---- SHAPE OF TRAINING DATA (85%) ----")
    print("X_train: ", X_train.shape)
    print("y_train: ", y_train.shape)
    print()
    print("---- SHAPE OF TESTING DATA (15%) ----")
    print("X_test: ", X_test.shape)
    print("y_test: ", y_test.shape)
    print()

    print("Traning Random Forest model....")
    print()
    model = RandomForestClassifier(n_estimators=args[0].n_estimators, random_state=args[0].random_state)
    model.fit(X_train, y_train)
    print()

    model_path = os.path.join(args[0].model_dir, "model.joblib")
    joblib.dump(model, model_path)
    print("Model persisted at location: ", model_path)
    print()


    y_pred = model.predict(X_test)
    test_acc = accuracy_score(y_test, y_pred)
    test_rep = classification_report(y_test, y_pred)

    print()
    print("---- Metrics Results For Testing Data ----")
    print()
    print("total Rows are: ", X_test.shape[0])
    print('[TESTING] Model Accuracy: ', test_acc)
    print('[TESTING] Classification Report: ')
    print(test_rep)




