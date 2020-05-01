from tinydb import *


def login(login_data, db):
    login_query = Query()
    if not db.get(login_query.name == login_data["user"]):
        print("User not in DB")
        db.insert({'ip': login_data["src"], 'reason': 'User not in Database'})
        # conn.close()
        return "wrong_user"
    elif not db.get(login_query.passwd == login_data["passwd"]):
        print("Password Incorrect")
        db.insert({'ip': login_data["src"], 'reason': 'wrong password'})
        # conn.close()
        return "wrong_password"
    else:
        print("Login with correct passwd")
    return 0
