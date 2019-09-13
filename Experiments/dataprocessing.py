import pandas as pd

def data_preprocessing(churn):
    churn = churn.drop('Phone', axis=1)
    churn['Area Code'] = churn['Area Code'].astype(object)
    churn = churn.drop(['Day Charge', 'Eve Charge', 'Night Charge', 'Intl Charge'], axis=1)
    model_data = pd.get_dummies(churn)
    return model_data