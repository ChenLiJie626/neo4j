import pandas
import csv, sqlite3
conn= sqlite3.connect("movie.db")
df = pandas.read_csv(r'D:\university courses\大三\创新实践\movies.csv')
df.to_sql('movie', conn, if_exists='append', index=False)
print('ok')