import mysql.connector

mydb = mysql.connector.connect(
  host="138.197.181.210",
  user="student_dreamers",
  passwd="1bJSe9hcO5Jkj2G2Klz7",
   database="student_dreamers"
)


mycursor = mydb.cursor()


sql = "INSERT INTO data_category (name, uuid) VALUES (%s, %s)"
val = ("Konečně", "to kurva funguje")

print(sql,val)
mycursor.execute(sql,val)

mydb.commit()

