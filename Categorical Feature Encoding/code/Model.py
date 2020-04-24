from Preprocessing import Dataset
from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, roc_auc_score

import pandas as pd
import numpy as np

import warnings
warnings.filterwarnings("ignore")

class Modeling:
    def __init__(self, X_train, y_train, set_seed):
        self.X = X_train
        self.y = y_train
        self.set_seed = set_seed

    def Logistic_Regression(self, X_test, ground_truth, return_type):
        print("Modeling..")
        model = LogisticRegression(random_state = self.set_seed, C = 0.1)
            
        model.fit(self.X, self.y)
        prediction = model.predict(X_test)            

        if return_type == "prediction":
            return prediction
            
        elif return_type == "accuracy":
            print("[Logistic Regression] Accuracy: {} ".format(accuracy_score(prediction, ground_truth)))
            return accuracy_score(prediction, ground_truth)

        elif return_type == 'auc':
            print("[Logistic Regression] AUC: {} ".format(roc_auc_score(prediction, ground_truth)))
            return roc_auc_score(prediction, ground_truth)

    def Random_Forest(self, X_test, ground_truth, return_type):
        ## Too late.. ###
        print("Modeling..")
        model = RandomForestClassifier(random_state = self.set_seed)
        
        model.fit(self.X, self.y)
        prediction = model.predict(X_test)
        print("[Random Forest] Accuracy : {}".format(accuracy_score(prediction, ground_truth)))

        if return_type == "prediction":
            return prediction

        elif return_type == "accuracy":
            return accuracy_score(prediction, ground_truth)

        elif return_type == 'auc':
            return roc_auc_score(prediction, ground_truth)