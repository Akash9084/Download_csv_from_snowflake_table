import pandas as pd
import snowflake.connector
import csv
username = '' #username_of_snowflake_account
password = '' #password_of_snowflake_account
account = '' #account_name
warehouse = '' #warehouse_name_of
database = '' #databse_nama
stage_table = '' #stage_table
ctx = snowflake.connector.connect(user=username, password=password, account=account)
def execute_query(ctx, query):
    cs = ctx.cursor()
    cs.execute(query)
    cs.close()
sql = 'use {}'.format(database)
execute_query(ctx, sql)
sql = 'use warehouse {}'.format(warehouse)
execute_query(ctx, sql)
cs = ctx.cursor()
query="select * from table_name"#write query to get data from
cs.execute(query)
df = cs.fetch_pandas_all()
df.to_csv('Name_of_output_file.csv.gz',
  sep=',',
  header=True,
  index=False,
  quoting=csv.QUOTE_ALL,
  compression='gzip',
  quotechar='"',
  doublequote=True,
  line_terminator='\n')
def execute_query(conn, query):
    cs = conn.cursor()
    cs.execute(query)
    cs.close()
