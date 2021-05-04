from app.config import host,port, database, user, password

import psycopg2

def conection():
    connection = psycopg2.connect(user=user, password=password, host=host, port=port, database=database)

if __name__ =='__main__':
    conection()