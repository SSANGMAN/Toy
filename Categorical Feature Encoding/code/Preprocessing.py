import numpy as np
import pandas as pd

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.feature_extraction import FeatureHasher
from sklearn.model_selection import train_test_split

class Dataset:
    def __init__(self, path, train):
        self.path = path
        self.train = train

        if self.train == True:
            self.df = pd.read_csv(path)
            self.X_train = self.df.drop(columns = ['id', 'target'])

            for col in self.X_train.columns:
                if self.X_train[col].dtype == 'int':
                    self.X_train[col] = self.X_train.astype('object')

            self.y_train = self.df['target']
        
        elif self.train == False:
            self.df = pd.read_csv(path)
            self.X_test = self.df.drop(columns = ['id'])

            for col in self.X_test.columns:
                if self.X_test[col].dtype == 'int':
                    self.X_test[col] = self.X_test.astype('object')
    
    def Feature_LabelEncoder(self, test_size = 0.2, train = None):
        if self.train == True:
            label_encoder = LabelEncoder()

            X_train, X_val, y_train, y_val = train_test_split(self.X_train, self.y_train, test_size = test_size, random_state = 42)

            for col in X_train.columns:
                X_train[col] = label_encoder.fit_transform(X_train[col])
                X_val[col] = label_encoder.fit_transform(X_train[col])

            if train == True:
                print("Train Data Shape : {} Rows, {} Columns".format(X_train.shape[0], X_train.shape[1]))
                return X_train, y_train

            else:
                print("Validation Data Shape : {} Rows, {} Columns".format(X_val.shape[0], X_val.shape[1]))
                return X_val, y_val
        
        elif self.train == False:
            lebel_encoder = LabelEncoder()
            X_test = self.X_test.copy()

            for col in self.X_test.columns:
                X_test[col] = label_encoder.fit_transform(X_test[col])    

            print("Test Data Shape : {} Rows, {} Columns".format(X_test.shape[0], X_test.shape[1]))
            return X_test

    def Feature_OneHotEncoder(self, test_size = 0.2, train = None):
        encoder = OneHotEncoder()
        if self.train == True:

            df_train = encoder.fit_transform(self.X_train)

            X_train, X_val, y_train, y_val = train_test_split(df_train, self.y_train, test_size = test_size, random_state = 42)
            
            if train == True:
                print("Train Data Shape : {} Rows, {} Columns".format(X_train.shape[0], X_train.shape[1]))
                return X_train, y_train

            else:
                print("Validation Data Shape : {} Rows, {} Columns".format(X_val.shape[0], X_val.shape[1]))
                return X_val, y_val
        
        elif self.test == False:
            X_test = self.X_test.copy()

            X_test = encoder.fit_transform(X_test)
            
            print("Test Data Shape : {} Rows, {} Columns".format(X_test.shape[0], X_test.shape[1]))
            return X_test

    def Feature_Hashing(self, test_size = 0.2, train = None):
        hashing_encoder = FeatureHasher(input_type = 'string')

        if self.train == True:
            for col in self.X_train.columns:
                if self.X_train[col].dtype == 'object':
                    self.X_train[col] = self.X_train[col].astype('str')

            train_df = hashing_encoder.fit_transform(self.X_train)

            X_train, X_val, y_train, y_val = train_test_split(train_df, self.ylabel, test_size = test_size, random_state = 42)
            
            if train == True:
                print("Train Data Shape : {} Rows, {} Columns".format(X_train.shape[0], X_train.shape[1]))
                return X_train, y_train

            else:
                print("Validation Data Shape : {} Rows, {} Columns".format(X_val.shape[0], X_val.shape[1]))
                return X_val, y_val

        elif self.train == False:
            X_test = self.X_test.copy()

            for col in X_test.columns:
                if X_test[col].dtype == 'object':
                    X_test[col] = self.X_test[col].astype('str')

            print("Test Data Shape : {} Rows, {} Columns".format(X_test.shape[0], X_test.shape[1]))
            return X_test

    def Feature_Stat(self, test_size = 0.2, train = None):
        if self.train == True:
            f = self.X_train.copy()

            for col in f.columns:
                f[col] = f[col].astype('category')
                counts = f[col].value_counts().sort_index().fillna(0)

                # 컬럼별 고유값 개수에 따른 Uniform 분포를 따르는 난수 생성 후, 각각 1000으로 나눈다. 그 후, 각 빈도수에 더한다.
                # 1000으로 나뉘는 이유는 같은 같은 빈도수가 등장하게 되면, 다른 범주여도 같은 범주로 인식을 할 수 있기 때문이다.
                # ex) 0과 1로 구성된 컬럼은 (2, ) 형태의 난수를 생성하고 각각을 1000으로 나눈후, 빈도에 더한다.
                
                counts += np.random.rand(len(counts)) / 1000
                f[col].cat.categories = counts

            X_train, X_val, y_train, y_val = train_test_split(f, self.y_train, test_size = test_size, random_state = 42)

            if train == True:
                print("Train Data Shape : {} Rows, {} Columns".format(X_train.shape[0], X_train.shape[1]))
                return X_train, y_train

            else:
                print("Validation Data Shape : {} Rows, {} Columns".format(X_val.shape[0], X_val.shape[1]))
                return X_val, y_val

        if self.train == False:
            X_test = self.X_test.copy()

            for col in X_test.columns:
                X_test[col] = X_test[col].astype('category')
                counts = X_test[col].value_counts().sort_imdex().fillna(0)
                counts += np.random.rand(len(count)) / 1000
                X_test[col].cat.categories = counts

            print("Test Data Shape : {} Rows, {} Columns".format(X_test.shape[0], X_test.shape[1]))            
            return X_test
    
    def Feature_Cyclic(self, test_size = 0.2, train = None):
        cyclic_cols = ['day', 'month']
        encoder = OneHotEncoder()

        if self.train == True:
            f = self.X_train.copy()

            for cyclic_col in cyclic_cols:
                f[cyclic_col] = f[cyclic_col].astype('float')

                f[cyclic_col + "_sin"] = np.sin((2 * np.pi * f[cyclic_col]) / max(f[cyclic_col]))
                f[cyclic_col + "_cos"] = np.cos((2 * np.pi * f[cyclic_col]) / max(f[cyclic_col]))

            f.drop(columns = cyclic_cols, inplace = True)
            
            oh_f = encoder.fit_transform(f)
            
            X_train, X_val, y_train, y_val = train_test_split(oh_f, self.y_train, test_size = test_size, random_state = 42)
            
            if train == True:
                print("Train Data Shape : {} Rows, {} Columns".format(X_train.shape[0], X_train.shape[1]))
                return X_train, y_train

            else:
                print("Validation Data Shape : {} Rows, {} Columns".format(X_val.shape[0], X_val.shape[1]))
                return X_val, y_val

        elif self.train == False:
            X_test = self.X_test.copy()

            for cyclic_col in cyclic_cols:
                X_test[cyclic_col + "_sin"] = np.sin((2 * np.pi * X_test[cyclic_col]) / max(X_test[cyclic_col]))
                X_test[cyclic_col + "_cos"] = np.cos((2 * np.pi * X_test[cyclic_col]) / max(X_test[cyclic_col]))

            X_test.drop(columns = cyclic_cols, inplace = True)

            X_test = encoder.fit_transform(X_test)

            print("Test Data Shape : {} Rows, {} Columns".format(X_test.shape[0], X_test.shape[1]))
            return X_test