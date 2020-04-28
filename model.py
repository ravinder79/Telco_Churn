
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
##%matplotlib inline
#%config InlineBackend.figure_formats = ['retina']
import seaborn as sns
import time
import warnings
warnings.filterwarnings("ignore")
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, log_loss, fbeta_score
from sklearn.metrics import auc, roc_curve, roc_auc_score, precision_recall_curve


def classification_summary(X, y, f, t):
    '''
    Returns classification report of a model
    '''
    y_pred = f.predict(X)
    y_pred_proba = f.predict_proba(X)
    y_pred_proba = pd.DataFrame(y_pred_proba, columns = ['no churn', 'churn'])
    yhat = (y_pred_proba > t).astype(int)
    print(classification_report(y, yhat.churn))

def generate_csv(X_df, df,f, t):
    '''
    Generates a csv showing churn prediction and churn probability for each customer
    '''
    y_pred_proba = f.predict_proba(X_df)
    y_pred_proba = pd.DataFrame(y_pred_proba, columns = ['no churn', 'churn_prob'], index = X_df.index)
    y_pred_proba['churn_prediction'] = (y_pred_proba.churn_prob > t).astype(int) 
    y_pred_proba = y_pred_proba.drop(columns = ['no churn'])
    final_csv = df[['customer_id']]
    final_csv = pd.merge(final_csv, y_pred_proba, left_index = True,right_index= True, how='left')
    return final_csv





