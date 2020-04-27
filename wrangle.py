import pandas as pd
import numpy as np
import sklearn


def wrangle_telco(df):
    df['total_charges'] = df['total_charges'].str.strip()
    df = df.replace(r'^\s*$', np.nan, regex=True)
    df = df.dropna()
    df.total_charges = df.total_charges.astype(float)
    df = df.replace('Yes', 1)
    df = df.replace('No', 0)
    df = df.replace('No internet service', 2)
    df['tenure_years'] = df.tenure/12
    df.tenure_years = df.tenure_years.apply(np.floor)
    return df

