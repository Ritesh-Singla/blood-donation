import mysql.connector
conn= mysql.connector.connect(
		host="localhost",
		user="username",
		passwd="password",
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