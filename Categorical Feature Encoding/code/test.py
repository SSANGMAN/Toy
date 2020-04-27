import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from code.Model import Modeling
from Preprocessing import Dataset


""" Test code """

def Result(metric):    
    path = 'data/'

    X_train, y_train = Dataset(path = path + 'train.csv', train = True).Feature_Hashing(test_size = 0.2, train = True)
    X_val, y_val = Dataset(path = path + 'train.csv', train = True).Feature_Hashing(test_size = 0.2 ,train = False)

    model = Modeling(X_train, y_train, set_seed = 42)

    prediction = model.Logistic_Regression(X_val, y_val, return_type = metric)

    return prediction
    
Result(metric = 'accuracy')