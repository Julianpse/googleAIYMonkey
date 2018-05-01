import psycopg2
import os
from os import environ
import json
from datetime import datetime
# Global vars below
  
username = environ.get('DATABASE_USERNAME', None)
access_key = environ.get('DATABASE_PASS', None)
database_endpoint= environ.get('DATABASE_ENDPOINT', None)

# These variables open the database connection
conn = psycopg2.connect(dbname='voice_monkey', user=username, host=database_endpoint, password=access_key)
cur = conn.cursor()

def connect_to_postgres():
    try:
        conn
        cur
    except:
        print("I am unable to connect to the database, please check your connection")
    return conn, cur


def insertTask(message):
    connect_to_postgres()
    cur.execute("INSERT INTO to_do_list VALUES (DEFAULT, '"+message+"');")
    conn.commit()
    cur.close()
    conn.close()
    
def changeStatus(iD):
    connect_to_postgres()
    cur.execute("SELECT status FROM to_do_list WHERE id="+str(iD)+";")
    state = cur.fetchone()[0]
    if(state == 'open'):
        cur.execute("UPDATE to_do_list SET status = 'closed' WHERE id= "+str(iD)+";")
        conn.commit()
        cur.close()
        conn.close()
    else:
        cur.execute("UPDATE to_do_list SET status = 'open' WHERE id= "+str(iD)+";")
        conn.commit()
        cur.close()
        conn.close()
        


def removeTask(iD):
    connect_to_postgres()
    cur.execute("DELETE FROM to_do_list WHERE id= "+str(iD)+";")
    conn.commit()
    cur.close()
    conn.close()

    
def openTasks():
    connect_to_postgres()
    cur.execute("SELECT id, task, status FROM to_do_list WHERE status = 'open' ORDER BY update_ts DESC;")
    rows = cur.fetchall()
    rowList = []
    for i in rows:
        a = list(i)
        rowList.append(a)
    rl = json.dumps(rowList)
    print(rl)
    return rl

def closedTasks():
    connect_to_postgres()
    cur.execute("SELECT id, task, status FROM to_do_list WHERE status = 'closed' ORDER BY update_ts DESC;")
    rows = cur.fetchall()
    rowList = []
    for i in rows:
        a = list(i)
        rowList.append(a)
    rl = json.dumps(rowList)
    print(rl)
    return rl
   
    

openTasks()
closedTasks()
