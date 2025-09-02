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


c.execute('''INSERT INTO products (product_id, product_name, price)
    VALUES
    (1, 'Computer', 800),
    (2, 'Telefone', 500),
    (3, 'Teclado', 300)

''')
conn.commit()

df_data2 = df_data.iloc[::-2]
df_data2.to_sql('data', conn, if_exists='append')

c.execute('''SELECT * FROM data''')
c.fetchall()
df = pd.DataFrame(c.fetchall())

c.execute('SELECT A, B, C FROM data WHERE A > 200 AND B > 100')
df = pd.DataFrame(c.fetchall())

query = 'SELECT * FROM data'
df = pd.read_sql(query, con=conn, index_col='index_name')




c.execute("UPDATE data SET A=218 WHERE index_name='b'")
conn.commit()
