import psycopg2
import os
from os import environ
# Global vars below
  
username = environ.get('DATABASE_USERNAME', None)
access_key = environ.get('DATABASE_PASS', None)
database_endpoint= environ.get('DATABASE_ENDPOINT', None)

# These variables open the database connection
conn = psycopg2.connect(dbname='voice_monkey', user=username, host=database_endpoint, password=access_key)
cur = conn.cursor()
print(cur)
def connect_to_postgres():
    try:
        conn
        cur
    except:
        print("I am unable to connect to the database, please check your connection")
    return conn, cur

cur.execute("INSERT INTO to_do_list VALUES (DEFAULT, 'Feed the cat at 5AM');")
conn.commit()
cur.close()
conn.close()