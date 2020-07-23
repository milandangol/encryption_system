class Data:
    def  __init__(self,website,passwords,users,email):
        self.website= website
        self.passwords = passwords
        self.users =users
        self.email = email
    def set_website(self,website):
        self.website = website
        return self.website
    def get_website(self):
        return self.website

    def set_passwords(self, passwords):
        self.passwords = passwords
        return self.passwords

    def get_passwords(self):
        return self.passwords

    def set_users(self, users):
        self.users = users
        return self.users

    def get_users(self):
        return self.users

    def set_email(self, email):
        self.email = email
        return self.email
    def get_email(self):
        return self.email