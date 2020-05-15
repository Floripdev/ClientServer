from tinydb import *


class db_handler:
    def __init__(self, db_path):
        self.db_path = db_path
        self.db = TinyDB(self.db_path)
        self.ask = Query()
        return

    def define_server_parameters(self, hostname, host_ip, port):
        if not self.db.search(self.ask.id == 0):
            self.db.insert({'id': 0, 'name': hostname,
                            'ip': host_ip, 'port': port})
        else:
            self.db.update({'ip': host_ip}, self.ask.id == 0)
            self.db.update({'name': hostname}, self.ask.id == 0)
        return

    def get_server_info(self):
        host_info = self.db.get(self.ask.id == 0)
        return host_info

    def get_user_info(self, client_name):
        client_info = self.db.get(self.ask.name == client_name)
        return client_info

    def insert_new_user(self, new_user, u_id):
        self.db.insert({'id': u_id, 'name': new_user['user'],
                        'ip': new_user['src'], 'passwd': new_user['passwd']})
        return

    def update_user_ip(self, user_info):
        self.db.update({'ip': user_info['ip']},
                       self.ask.name == user_info['name'])
        return

    def update_user_password(self, user_info):
        self.db.update(
            {'passwd': user_info['passwd']}, self.ask.name == user_info['name'])
        return

    def user_login(self, login_data):
        if not self.db.get(self.ask.name == login_data['user']):
            print("User not in db")
            self.db.insert(
                {"ip": login_data['src'], 'reason': 'User not in db'})
            return "wrong_user"
        elif not self.db.get(self.ask.passwd == login_data['passwd']):
            print("Password Incorrect")
            self.db.insert(
                {"ip": login_data['src'], 'reason': 'Wrong Password'})
            return "wrong_password"
        else:
            print("Login with correct password")
            return 0
