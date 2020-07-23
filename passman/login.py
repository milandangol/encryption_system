from passman.connection import connection
class login:
    def __init__(self):
        self.mydb = connection()

    def show_data_one(self,user):
        qry="SELECT * FROM register WHERE users = %s"
        values=(user,)
        data= self.mydb.show_one_data(qry,values)
        return data

    def return_keys(self, key):
        qry = "SELECT  users FROM confidential WHERE r_key = %s"
        values = (key,)
        bytes_keys = self.mydb.show_one_data(qry, values)
        return bytes_keys

    def update_password(self, password, users):
        qry = "UPDATE register SET password=%s WHERE users = %s"
        values = (password,users,)
        self.mydb.insert(qry, values)
        return True
