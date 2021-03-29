import mysql.connector
conn= mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="ratsi@123",
		database="blood")

c=conn.cursor()

c.execute(""" CREATE TABLE donors(
  		Full_name text,
  		Gender text,
  		Blood_Group text,
  		Address text,
  		Contact integer,
  		City text,
  		State text,
  		Zip_code integer
  						)
  			""")