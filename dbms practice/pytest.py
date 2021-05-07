import pandas as pd
from sqlalchemy import create_engine
cols = [2,3]
df = pd.read_excel('EmployeeList.xlsx', engine='openpyxl',usecols=cols)

engine = create_engine('mysql+mysqlconnector://root:oreo0008@localhost/practice'.format(user='root', password='oreo0008', server='localhost', database='practic'))

df.to_sql('people', con=engine) 
# /* to make any queries in database form python file */
# query=''' .....''''
# df=pd.read_sql_query(query,engine)

#/* name of sql coloumn n csv file coloumn should be same , can be achieved in python file by */
 #df.rename(columns={
 #  'oldname': 'newname'
 # }inplace=True)

 
