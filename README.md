# Telco Churn prediction using Classification 

## Team Members: Cameron Taylor and Ravinder Singh

## Deliverables
* A report (ipynb) answering the question, "Why are our customers churning?" 

* CSV with the customer_id, probability of churn, and the prediction of churn (1=churn, 0=not_churn).

*  1-3 google slides (+ title) that illustrates how your model works, including the features being used

* A .py file that will take in a new dataset, and perform all the transformations necessary to run the model you have developed on this new dataset to provide probabilities and predictions.

## SQL Data Acquisition 
Must use your own env file to access data.

## Technical Skills used

* Python
* SQL
* Various data science libraries (Pandas, Numpy, Matplotlib, seaborn etc)
* Stats (Hypothesis testing, correlation tests)
* Classification Metholdogies (Logistic Regression, KNN, Decision Tree, Random Forest)

## Data Dictionary

payment_type_id:              7043 non-null int64  (payment type id)\

internet_service_type_id  :  7043 non-null int64 (type of internet service subscribed)\

contract_type_id    :        7043 non-null int64 (type of contract, month-to-month, one year, two year)\
customer_id       :          7043 non-null object (unique customer ID)\
gender            :          7043 non-null object (male or female)\
senior_citizen    :          7043 non-null int64  (senior citizen or not)\
partner           :          7043 non-null object (have partner or is single)\
dependents        :          7043 non-null object (has dependents or not)\
tenure            :          7043 non-null int64 (how long with company in months)\
phone_service     :          7043 non-null object (has phone service or not)\
multiple_lines     :         7043 non-null object (has multiple phone lines or  not)\
online_security    :         7043 non-null object (have online security service subscribed)\
online_backup     :          7043 non-null object (have online backup service subscribed)\
device_protection :          7043 non-null object (have device_protection service subscribed)\
tech_support        :        7043 non-null object (have tech_support service subscribed)\
streaming_tv       :         7043 non-null object (streams tv)\
streaming_movies   :         7043 non-null object (streams movies)\
paperless_billing   :        7043 non-null object (have paperless billing)\
monthly_charges    :         7043 non-null float64 (monthly charges)\
total_charges      :         7043 non-null object (total charges during the tenure)\
churn              :         7043 non-null object (whether churned or not)\
contract_type      :         7043 non-null object (contract type month-to-month, one year, two year)\
internet_service_type  :     7043 non-null object (Fiber optic, DSL or none as service)\
payment_type         :       7043 non-null object (type of payment method used by subscriber)\

# Files in this repo you need to run this (you will need your own env file)
* acquire_r.py
* wrangle.py
* evaluate.py
* preprocess.py
* models.py
* logistic_regression_util.py
* knn_lesson_util.py
* Telco_Churn_Final.ipynb (Main notebook)

# Executive Summary
* We created a logistic regression model to predict customers who are likely to churn.
* The model is able to correctly predict 80% of customers who actually churn.
* Customers most likely to churn:\
** Month to month contract\
** New customers (tenure less than 2 years)\
** Have fiber optic internet
* Focus resources on retaining ‘new’ customers since company does fine retaining the longer tenured customers



# Summary of findings
See the link below for summary slides

https://docs.google.com/presentation/d/1ODagzmh01di-fNy54dmKlKO4DzZ1UNsL3oVOOEth95E/edit?usp=sharing

