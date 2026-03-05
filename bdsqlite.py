import sqlite3
import pandas as pd

conn=sqlite3.connect('db.db')

df = pd.read_csv('Contoso - Vendas - 2017.csv', index_col=0)
df.index.name = 'Numero da Venda'
#df.to_sql(df,conn,index_label='Numero da Venda')
df
#c=conn.cursor()
#conn.commit()