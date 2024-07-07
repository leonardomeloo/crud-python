import mysql.connector

connection = mysql.connector.connect(user='root', 
                                     password='admin',
                                     host='localhost',
                                     database='crud_python')
connection.cursor()