import sys
sys.path.append('./code')

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from Model import Modeling
from Preprocessing import Dataset
""" Test code """

def Result(metric, preprocessing = 'all', view = True):
    if preprocessing == 'all':
        metric_list = []
        preprocessing_method = ['LabelEncoder', 'OneHotEncoder', 'Feature Hashing', 'Statistics', 'Cyclic Encoding']
        
        path = 'data/'
        raw_data = Dataset(path = path + 'train.csv', train = True)
        
        count = 1

        for _ in range(len(preprocessing_method)):
            if count == 1:
                print("Label Encoder")
                X_train, y_train = raw_data.Feature_LabelEncoder(test_size = 0.2, train = True)
                X_val, y_val = raw_data.Feature_LabelEncoder(test_size = 0.2, train = False)

            elif count == 2:
                print("One Hot Encoder")
                X_train, y_train = raw_data.Feature_OneHotEncoder(test_size = 0.2, train = True)
                X_val, y_val = raw_data.Feature_OneHotEncoder(test_size = 0.2, train = False)
                
            elif count == 3:
                print("Feature Hashing")
                X_train, y_train = raw_data.Feature_Hashing(test_size = 0.2, train = True)
                X_val, y_val = raw_data.Feature_Hashing(test_size = 0.2, train = False)

            elif count == 4:
                print("Statistic Method")
                X_train, y_train = raw_data.Feature_Stat(test_size = 0.2, train = True)
                X_val, y_val = raw_data.Feature_Stat(test_size = 0.2, train = False)

            elif count == 5:
                print("Cyclic Encoding")
                X_train, y_train = raw_data.Feature_Cyclic(test_size = 0.2, train = True)
                X_val, y_val = raw_data.Feature_Cyclic(test_size = 0.2, train = False)

            model = Modeling(X_train, y_train, set_seed = 42)

            prediction = model.Logistic_Regression(X_val, y_val, return_type = metric)
        
            metric_list.append(prediction)

            count += 1

        if view == True:

            # Comparision Visualization
            plot = sns.barplot(x = preprocessing_method, y = metric_list)
            plot.set_xticklabels(plot.get_xticklabels(), rotation = 15)

            if metric == 'accuracy':
                plot.set_ylabel("Accuracy")

            elif metric == 'auc':
                plot.set_ylabel('AUC')

            plt.show()        
    else:
        pass
    
Result(metric = 'accuracy', preprocessing = 'all')
""""""""""""""""""