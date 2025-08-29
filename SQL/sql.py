import sqlite3
import pandas as pd

conn = sqlite3.connect('web.db')

df_data = pd.read_csv('bd_data.csv', index_col=0)
df_data.index.name = 'index_name'
df_data.to_sql('data', conn, index_label='index_name')

c = conn.cursor()
c.execute('CREATE TABLE products (product_id, product_name, price)')
conn.commit()

c.execute('DROP TABLE products')
c.execute('DROP TABLE data')

c.execute('CREATE TABLE products ([product_id] INTEREGER PRIMARY KEY, [product_name] TEXT, [price] INTEREGER)')