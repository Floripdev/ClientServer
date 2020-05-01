def create_account(data):
    print("****Creating Account*****")
    clientname = input("Insert Login: ")
    passwd = input("Insert Password: ")
    data["user"] = clientname
    data["passwd"] = passwd
    data["type"] = "init_create"
    data["msg"] = "null"
    return data
