import pandas as pd
from sqlalchemy import create_engine

df = pd.read_excel('EmployeeList.xlsx', engine='openpyxl')

engine = create_engine('mysql+mysqlconnector://root:oreo0008@localhost/practice'.format(user='root', password='oreo0008', server='localhost', database='practice'))
df.to_sql('people', con=engine)