## Countries Information Ingestion 
### Overview
This project focuses on building an ETL (Extract, Transform, Load) pipeline for data from the REST Countries API using Python. The pipeline extracts information such as country names, languages, currencies, regions etc., transforms the data, and loads it in a PostgreSQL database. The project also includes data analysis through SQL queries and visualization using Power BI.
### Technologies
1.	Programming Language: Python 3.12
2.	Database: PostgreSQL
3.	Visualization: Power BI
4.	Version Control: Git
5.	API: Rest Country API

### Architecture Design and Workflow
![image](https://github.com/user-attachments/assets/4e10dde3-892a-4cdc-9fb4-f702884e6f28)

*	Use Python scripts to call the Rest countries API endpoint.
*	Store the raw JSON responses temporarily.
*	Process the JSON data using pandas and store in a dataframe.
*	Design PostgreSQL schemas for country data.
*	Load the transformed data into PostgreSQL tables using sqlalchemy and psycopg2.
* Perform analysis in PostgreSQL to insight of the data
*	Connect Power BI to the PostgreSQL database.
*	Create dashboards with KPIs such as Total number of countries etc.



