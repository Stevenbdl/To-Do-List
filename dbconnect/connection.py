import mysql.connector

#MySQL connection
connection = mysql.connector.connect(
    host='localhost',
    user='steven',
    password='8294403049Steven',
    database='to_do_list'
)


cursor = connection.cursor()


