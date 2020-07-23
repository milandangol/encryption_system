from Crypto.Cipher import AES
from passman.connection import connection
import binascii

class file:
    def __init__(self):
        self.buffer = 32000
        self.mydb = connection()
    def return_keys(self, user):
        qry = "SELECT  r_key FROM confidential WHERE users = %s"
        values = (user,)
        bytes_keys = self.mydb.show_data(qry, values)
        return bytes_keys
    def encrpyt(self,key,filename):
        keys = binascii.unhexlify(key)
        user_file = open(filename,"rb")
        encrypt_file=open(filename + '.encrypted', 'wb')
        cipher_file = AES.new(keys,AES.MODE_OFB)
        encrypt_file.write(cipher_file.iv)
        buffer = user_file.read(self.buffer)
        while len(buffer)>0:
            cypher_byte = cipher_file.encrypt(buffer)
            encrypt_file.write(cypher_byte)
            buffer=user_file.read(self.buffer)
        user_file.close()
        encrypt_file.close()
        return True
    def img_to_binary(self,filename):
        with open(filename, 'rb') as file:
            binaryData = file.read()
        return binaryData
    def encrypt_save(self,users,files,file_name):
        qry= "INSERT INTO file_database(users,files,file_name) VALUES(%s,%s,%s)"
        value=(users,files,file_name)
        self.mydb.insert(qry,value)
        return True

    def retrive_img_file_name(self,users):
        qry  = "SELECT * FROM file_database WHERE users=%s"
        value = (users,)
        data =self.mydb.show_data(qry,value)
        return data
    def retrive_img(self,users,file_name):
        qry="SELECT * FROM file_database WHERE users=%s AND file_name=%s"
        value = (users,file_name)
        data = self.mydb.show_data(qry,value)
        return  data

    def write_file(self,filename, data):
        with open(filename, 'wb') as file:
            file.write(data)
            return True
    def decrypt(self,filename,Key):
        newKey= binascii.unhexlify(Key)
        input_file = open(filename, 'rb')
        output_file = open(filename + '.decrypted', 'wb')
        iv = input_file.read(16)
        cipher_encrypt = AES.new(newKey, AES.MODE_OFB, iv=iv)
        buffer = input_file.read(self.buffer)
        while len(buffer) > 0:
            decrypted_bytes = cipher_encrypt.decrypt(buffer)
            output_file.write(decrypted_bytes)
            buffer = input_file.read(self.buffer)
        input_file.close()
        output_file.close()
        return True