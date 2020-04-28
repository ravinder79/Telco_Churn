import numpy as np
import sklearn
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, MinMaxScaler
import pandas as pd

def encode(df, l):
    '''
    OneHot encodes the data in a column or columns
    '''
    encoder = sklearn.preprocessing.OneHotEncoder(sparse = False)
    encoder.fit(df[l])
    m = encoder.transform(df[l])
    col_name= encoder.get_feature_names(l)
    df = pd.concat([df, pd.DataFrame(m, columns = col_name,index = df.index)], axis =1)
    df = df.drop(columns = l)
    return df

def scale_minmax(train, column_list):
    '''
    MinMax scales the data in a column or columns
    '''
    scaler = MinMaxScaler()
    column_list_scaled = [col + '_scaled' for col in column_list]
    train_scaled = pd.DataFrame(scaler.fit_transform(train[column_list]), 
                                columns = column_list_scaled, 
                                index = train.index)
    train = train.join(train_scaled)
    train = train.drop(columns = column_list)
    return train

def features(train, validate, test, l):
    '''
    Splits train, validate, and test sets into their respective X and y dataframes for use in modeling
    '''
    y_train = train[['churn']]
    y_validate = validate[['churn']]
    y_test = test[['churn']]
    X_train = train[l]
    X_validate = validate[l]
    X_test = test[l]
    return X_train, X_validate, X_test, y_train, y_validate, y_test