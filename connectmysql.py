import mysql.connector
def connectToSQL():
    try:
        SQLConnection = mysql.connector.connect(
            host="localhost",
            user="cpeoop",
            password="123123",
            database="mysqldemo"
        )
        return SQLConnection
    except:
        print("An error occured, please check your database connection.")
        return None