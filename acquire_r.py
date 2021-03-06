import pandas as pd
import numpy as np
import env


def get_db_url(database):
    '''
    This function returns a url required to retrieve data from the SQL database
    '''
    from env import host, user, password
    url = f'mysql+pymysql://{user}:{password}@{host}/{database}'
    return url

def get_data_from_sql():
    '''
    This function creates and returns a dataframe holding the data from the SQL 
    database specified
    '''
    query = """
    SELECT * FROM customers
    JOIN contract_types USING (contract_type_id)
    JOIN `internet_service_types` USING (internet_service_type_id)
    JOIN payment_types USING (payment_type_id)
    """
    df = pd.read_sql(query, get_db_url('telco_churn'))
    return df