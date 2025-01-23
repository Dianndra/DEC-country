from get_data import get_country_data
from sqlalchemy import create_engine
import pandas as pd
import os


def load_country_data(df, table_name, hostname, database, username, password, port):
    try:
        engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{hostname}:{port}/{database}')
        df.to_sql(table_name, engine, index=False, if_exists='replace')  
        
        return print("DataFrame loaded successfully into PostgreSQL database")
        
    except Exception as error:
        print("Error:", error)
    
hostname = 'localhost'
database = 'country_dw'
username = 'postgres'
password = os.getenv("MY_SECURE_PASSWORD")
port = '5432'
df = get_country_data()
table_name = 'country_data'

df.to_csv('../DEC-country/data/country_data.csv', index=False)

load_country_data(df, table_name, hostname, database, username, password, port)