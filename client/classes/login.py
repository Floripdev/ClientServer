def login_account(data):
    print("****Login Account*****")
    clientname = input("Insert Login: ")
    passwd = input("Insert Password: ")
    data["user"] = clientname
    data["passwd"] = passwd
    data["type"] = "init_login"
    data["msg"] = "null"
    return data
