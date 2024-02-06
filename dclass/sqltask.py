import sys
ID = sys.argv[1]
dcoin = sys.argv[2]
import mysql.connector

def dcoin_up(id_users, howmany):
    host = 'localhost'

    cnx = mysql.connector.connect(user='root',
                                  password='/32982302Marz_',
                                  host=host,
                                  database='dclass')

    cursor = cnx.cursor()
    query = "SELECT * FROM table_users"
    cursor.execute(query)
    values = [row for row in cursor]
    
    if any(id_users in row for row in values):
        query = f"UPDATE table_users SET dcoin = dcoin + {howmany} WHERE ID = '{id_users}'"
        cursor.execute(query)
    else:
        query = f"INSERT INTO table_users(ID, dcoin) VALUES('{id_users}', {howmany})"
        cursor.execute(query)

    cnx.commit()
    cursor.close()
    cnx.close()

if __name__ == '__main__':
    dcoin_up(ID, dcoin)
