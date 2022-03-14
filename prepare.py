import pandas as pd
import env 
import os
import acquire

'''
Using the Iris Data: 
 - Use the function defined in acquire.py to load the iris data. 
 - Drop the species_id and measurement_id columns.Rename the species_name column to just species.
 - Create dummy variables of the species name and concatenate onto the iris dataframe. (This is for practice, we don't always have to encode the target, but if we used species as a feature, we would need to encode it).
 - Create a function named prep_iris that accepts the untransformed iris data, and returns the data with the transformations above applied.
'''

def prep_iris(df):
        columns_to_drop = ['species_id', 'measurement_id']
        df = df.drop(columns = columns_to_drop)
        df = df.rename(columns={'species_name' : 'species'})
        dummy_df = pd.get_dummies(df[['species']],
                                 dummy_na=False,
                                 drop_first = [True])
        df = pd.concat([df, dummy_df], axis=1)
        return df

'''
Using the Titanic dataset
Use the function defined in acquire.py to load the Titanic data.
Drop any unnecessary, unhelpful, or duplicated columns.
Encode the categorical columns. Create dummy variables of the categorical columns and concatenate them onto the dataframe.
Create a function named prep_titanic that accepts the raw titanic data, and returns the data with the transformations above applied.
'''


def prep_titanic(df):
    df.drop_duplicates(inplace=True)
    columns_to_drop = ['deck', 'age', 'embarked', 'class', 'passenger_id']
    df = df.drop(columns = columns_to_drop)
    dummy_df = pd.get_dummies(df[['sex', 'embark_town']],
                         dummy_na=False,
                         drop_first = [True, True])
    df = pd.concat([df, dummy_df], axis=1)
    return df


'''
Using the Telco dataset
Use the function defined in acquire.py to load the Telco data.
Drop any unnecessary, unhelpful, or duplicated columns. This could mean dropping foreign key columns but keeping the corresponding string values, for example.
Encode the categorical columns. Create dummy variables of the categorical columns and concatenate them onto the dataframe.
Create a function named prep_telco that accepts the raw telco data, and returns the data with the transformations above applied.
'''

def prep_telco(df):
    columns_to_drop = ['payment_type_id', 'internet_service_type_id', 'contract_type_id', 'customer_id']                   
    df = df.drop(columns = columns_to_drop)
    dummy_df = pd.get_dummies(df[['contract_type', 'internet_service_type', 'payment_type']],
                          dummy_na=False,
                         drop_first = [True, True, True])
    df = pd.concat([df, dummy_df], axis=1)
    return df


def train_validate_test_split(df, target, seed=123):
    '''
    This function takes in a dataframe, the name of the target variable
    (for stratification purposes), and an integer for a setting a seed
    and splits the data into train, validate and test. 
    Test is 20% of the original dataset, validate is .30*.80= 24% of the 
    original dataset, and train is .70*.80= 56% of the original dataset. 
    The function returns, in this order, train, validate and test dataframes. 
    '''
    train_validate, test = train_test_split(df, test_size=0.2, 
                                            random_state=seed, 
                                            stratify=df[target])
    train, validate = train_test_split(train_validate, test_size=0.3, 
                                       random_state=seed,
                                       stratify=train_validate[target])
    return train, validate, test