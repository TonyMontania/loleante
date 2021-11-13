import mysql.connector

try: 
  mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='lol'
  )
  mycursor = mydb.cursor()
except mysql.connector.errors.DatabaseError:
  print("No se pudo conectar a la base de datos...")
  mydb = None
  mycursor = None

def EjecutarSQL(sql):
  mycursor.execute(sql) #Execute para ejecutar solo sentencias
  mydb.commit()

def EjecutarSQL_VAL(sql,val): 
  mycursor.executemany(sql, val) #ExecuteMany para ejecutar sentencias y variables
  mydb.commit()

def Mostrar(Parametro):
  mycursor.execute(Parametro) 
  myresult = mycursor.fetchall()
  for x in myresult:
    print(x) 