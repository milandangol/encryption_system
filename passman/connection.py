import  mysql.connector
class connection:
    def __init__(self):
        self.myconnection=mysql.connector.connect(user="root",password="",host="localhost",database='passman')
        self.my_cursor = self.myconnection.cursor()
    def insert(self,qry,values):
        self.my_cursor.execute(qry,values)
        self.myconnection.commit()
    def show_data(self,qry,values):
        self.my_cursor.execute(qry,values)
        data = self.my_cursor.fetchall()
        return data
    def show_one_data(self,qry,values):
        self.my_cursor.execute(qry,values)
        data = self.my_cursor.fetchone()
        return data