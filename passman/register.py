from passman.connection import connection
import os
from Crypto.Hash import SHA256
import re
class register:
    def __init__(self):
        self.mydb= connection()
    def add_user(self,user,password,first,last,email):
        qry = "INSERT INTO register (users , password, first_name , last_name, email ) VALUES (%s,%s,%s,%s,%s)"
        values = (user,password,first,last,email)
        self.mydb.insert(qry,values)
        return True
    def random_keys(self):
        self.keys = os.urandom(16)
        return self.keys
    def insert_key(self,users,keys):
        qry="INSERT INTO confidential (users ,r_key ) VALUES(%s,%s)"
        values = (users, keys,)
        self.mydb.insert(qry, values)
        return True
    def hash_user(self,user):
        hash_object = SHA256.new()
        hash_object.update(f"{user}".encode('utf-8'))
        hashed_user = hash_object.hexdigest()
        return hashed_user
    def check_email(self,email):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        resutl = re.search(regex,email)
        return resutl





