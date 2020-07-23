from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from passman.connection import connection
import  bcrypt
import  binascii
class manager:
    def __init__(self):
        self.mydb = connection()

    def add_data(self,website,passwords,users,email):
        qry = "INSERT INTO datas (website, passwords,users,email ) VALUES (%s,%s,%s,%s)"
        values = (website,passwords,users,email,)
        self.mydb.insert(qry, values)
        return True
    def show_data(self,user):
        qry = "SELECT * FROM datas WHERE users = %s"
        values =(user,)
        passwd = self.mydb.show_data(qry,values)
        return passwd
    def show_passsword(self,users,website):
        qry = "SELECT passwords FROM datas WHERE users = %s AND  website = %s   "
        values =(users,website)
        all_items = self.mydb.show_data(qry,values)
        return all_items
    def delete_data(self):
        pass
    def update_password(self,website,password,email,users):
        qry = "UPDATE datas SET website = %s, passwords = %s ,email =%s WHERE users = %s"
        values= (website,password,email,users,)
        self.mydb.insert(qry,values)
        return  True
    def return_keys(self,user):
        qry = "SELECT  r_key FROM confidential WHERE users = %s"
        values = (user,)
        bytes_keys = self.mydb.show_data(qry,values)
        return bytes_keys
    def passwd_encrpt(self,key,data):
        hex_keys = binascii.unhexlify(key)
        cipher1 = AES.new(hex_keys, AES.MODE_ECB)
        datas = data.encode("utf-8")
        ct = cipher1.encrypt(pad(datas, 16)).hex()
        return  ct
    def passwd_decpt(self,cipher,key):
        hex_keys = binascii.unhexlify(key)
        value = binascii.unhexlify(cipher)
        decipher = AES.new(hex_keys, AES.MODE_ECB)
        pt = unpad(decipher.decrypt(value), 16).decode('utf-8')
        return pt
    def salt_passwd(self,passwords):
        salt_pass = bcrypt.hashpw(passwords,bcrypt.gensalt())
        return salt_pass 