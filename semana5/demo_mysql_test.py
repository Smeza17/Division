import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="smeza",
  password="Chaohola",
  database="ejercicio2db"
)


mycursor = mydb.cursor()
mycursor.execute("show databases")
for i in mycursor:
  print(i)