#!/usr/bin/env python3
"""
Train the poverty predictor on a real dataset.

USAGE
-----
1. Place your training dataset at:  data/training_data.csv
   Required columns (values shown in parentheses):
     - householdSize     (integer, number of household members)
     - residence          (1 = Urban, 0 = Rural)
     - waterSource         (1 = Safe/piped, 0 = Unsafe)
     - toiletType           (1 = Improved/flush, 0 = Unimproved)
     - hasElectricity        (1/0)
     - hasMobilePhone         (1/0)
     - hasRadio                (1/0)
     - hasTelevision             (1/0)
     - hasRefrigerator            (1/0)
     - hasBicycle                  (1/0)
     - hasMotorcycle                 (1/0)
     - hasCar                          (1/0)
     - classification                    ('poor' or 'non-poor')  <-- target/label column

2. Run:  python train_model.py

This fits a scikit-learn LogisticRegression model, evaluates it on a held-out
test split, and writes the learned intercept/coefficients to
models/model_coefficients.json. models/predictor.py automatically picks up
that file the next time the app starts (or call model.reload() at runtime).
"""

import json
import os
import sys

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

FEATURE_ORDER = [
    'householdSize', 'residence', 'waterSource', 'toiletType',
    'hasElectricity', 'hasMobilePhone', 'hasRadio', 'hasTelevision',
    'hasRefrigerator', 'hasBicycle', 'hasMotorcycle', 'hasCar',
]

DATA_PATH = os.path.join('data', 'training_data.csv')
OUTPUT_PATH = os.path.join('models', 'model_coefficients.json')


def main():
    if not os.path.exists(DATA_PATH):
        print(f"ERROR: no training dataset found at '{DATA_PATH}'.")
        print("Place your TDHS-style CSV there (see the docstring at the top")
        print("of this file for the required columns) and re-run this script.")
        sys.exit(1)

    df = pd.read_csv(DATA_PATH)

    missing = [c for c in FEATURE_ORDER + ['classification'] if c not in df.columns]
    if missing:
        print(f"ERROR: dataset is missing required column(s): {missing}")
        sys.exit(1)

    X = df[FEATURE_ORDER].astype(float)
    y = (df['classification'].astype(str).str.strip().str.lower() == 'poor').astype(int)

    if y.nunique() < 2:
        print("ERROR: the 'classification' column only contains one class.")
        print("Both 'poor' and 'non-poor' examples are needed to train a model.")
        sys.exit(1)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    clf = LogisticRegression(max_iter=1000, class_weight='balanced')
    clf.fit(X_train, y_train)

    train_acc = accuracy_score(y_train, clf.predict(X_train))
    test_acc = accuracy_score(y_test, clf.predict(X_test))

    print(f"Train accuracy: {train_acc:.3f}")
    print(f"Test accuracy:  {test_acc:.3f}")
    print()
    print("Test set classification report:")
    print(classification_report(y_test, clf.predict(X_test), target_names=['non-poor', 'poor']))
    print("Confusion matrix (rows=actual, cols=predicted) [non-poor, poor]:")
    print(confusion_matrix(y_test, clf.predict(X_test)))

    coefficients = {name: float(coef) for name, coef in zip(FEATURE_ORDER, clf.coef_[0])}
    output = {
        'intercept': float(clf.intercept_[0]),
        'coefficients': coefficients,
        'trained': True,
        'train_accuracy': round(train_acc, 4),
        'test_accuracy': round(test_acc, 4),
        'n_train': int(len(X_train)),
        'n_test': int(len(X_test)),
    }

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w') as f:
        json.dump(output, f, indent=2)

    print(f"\nSaved trained coefficients to {OUTPUT_PATH}")
    print("Restart the Streamlit app (or call model.reload()) to use them.")


if __name__ == '__main__':
    main()
