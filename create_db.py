import mysql.connector
# function for creating database and connecting to database.
def create_db():
    mydb = mysql.connector.connect(host="localhost", user="root",password="oramca",database="mydatabase")
    mycursor = mydb.cursor()

    cursor = mydb.cursor()
    cursor.execute("CREATE TABLE employee (eid int PRIMARY KEY AUTO_INCREMENT, name varchar(255), email varchar(255), gender varchar(255), contact int, dob varchar(255), doj varchar(255), pass varchar(255), utype varchar(255), address varchar(255), salary int)")
    mydb.commit()


    
create_db()
