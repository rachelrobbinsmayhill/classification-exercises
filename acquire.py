
import pandas as pd
import env 
import os


# Can use global variables like below, or place them inside the function, as I did. 
# url_titanic = f'mysql+pymysql://{env.user}:{env.password}@{env.host}/titanic_db'
# url_iris = f'mysql+pymysql://{env.user}:{env.password}@{env.host}/iris_db'
# url_telco = f'mysql+pymysql://{env.user}:{env.password}@{env.host}/telco_churn' 


'''
Make a new python module, acquire.py to hold the following data aquisition functions:

1. Make a function named get_titanic_data that 
returns the titanic data from the codeup data science database 
as a pandas data frame. 

Obtain your data from the Codeup Data Science Database.

'''
#%%
def get_titanic_data(use_cache=True):
    filename = 'titanic.csv'
    
    if os.path.exists(filename):
        print('Reading from csv file...')
        return pd.read_csv(filename)
    
    url = f'mysql+pymysql://{env.user}:{env.password}@{env.host}/titanic_db'
    query = '''
    SELECT * 
        FROM passengers
        
    '''

    print('Getting a fresh copy from SQL database...')
    df = pd.read_sql(query, url)
    print('Saving to csv...')
    df.to_csv(filename, index=False)
    return df
#%%
get_titanic_data()
#%%



'''
2. Make a function named get_iris_data 
that returns the data from the iris_db 
on the codeup data science database as a pandas data frame. 
The returned data frame should include 
the actual name of the species 
in addition to the species_ids. 
Obtain your data from the Codeup Data Science Database.
'''
#%%
def get_iris_data(use_cache=True):
    filename = 'iris.csv'
    
    if os.path.exists(filename):
        print('Reading from csv file...')
        return pd.read_csv(filename)
    
    
    url = f'mysql+pymysql://{env.user}:{env.password}@{env.host}/iris_db'
    query = '''
     SELECT *
        FROM measurements
        JOIN species USING (species_id)
        
    '''

    print('Getting a fresh copy from SQL database...')
    df = pd.read_sql(query, url)
    print('Saving to csv...')
    df.to_csv(filename, index=False)
    return df
#%%
get_iris_data()
#%%




'''
3. Make a function named get_telco_data 
that returns the data from the telco_churn database in SQL. 
In your SQL, be sure to join all 4 tables together, so that 
the resulting dataframe contains all the contract, payment, and internet service options. Obtain your data from the Codeup Data Science Database.
'''
#%%
def get_telco_data(use_cache=True):
    filename = 'telco_churn.csv'
    
    if os.path.exists(filename):
        print('Reading from csv file...')
        return pd.read_csv(filename)
    
    
    url = f'mysql+pymysql://{env.user}:{env.password}@{env.host}/telco_churn'
    query = '''
    SELECT * 
        FROM customers
        JOIN contract_types 
        USING (contract_type_id)
        JOIN internet_service_types
        USING (internet_service_type_id)
        JOIN payment_types AS pt
        USING (payment_type_id)

        
    '''

    print('Getting a fresh copy from SQL database...')
    df = pd.read_sql(query, url)
    print('Saving to csv...')
    df.to_csv(filename, index=False)
    return df
#%%
get_telco_data()





'''
4. Once you've got your get_titanic_data, get_iris_data, and get_telco_data functions 
written, now it's time to add caching to them. 
To do this, edit the beginning of the function 
to check for the local filename of telco.csv, 
titanic.csv, or iris.csv. 
If they exist, use the .csv file. 

If the file doesn't exist, then produce the SQL and pandas necessary 
to create a dataframe, then write the dataframe to a .csv file 
with the appropriate name.

Make sure your env.py and csv files are not being pushed to GitHub!
'''
#%%

# Done




import os

def get_number_data():
    filename = 'numbers.csv'
    
    if os.path.exists(filename):
        print('Reading from csv file...')
        return pd.read_csv(filename)
    
    database = 'numbers'
    url = f'mysql+pymysql://{env.user}:{env.password}@{env.host}/{database}'
    query = '''
    SELECT
        
    '''

    print('Getting a fresh copy from SQL database...')
    df = pd.read_sql(query, url)
    print('Saving to csv...')
    df.to_csv(filename, index=False)
    return df
# %%
