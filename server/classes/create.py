def create(new_user_data, db):
    print("create class")
    db.insert({'id': 1, 'name': new_user_data["user"],
               'IP': new_user_data["src"], 'passwd': new_user_data["passwd"]})
    return
