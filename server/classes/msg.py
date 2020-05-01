def msg_welcome(s_entry, u_entry, data):
    data["msg"] = f"Welcome to the {s_entry.get('name')} {u_entry.get('name')}! :) connected to {s_entry.get('ip')} on Port: {s_entry.get('port')}"
    data["type"] = "notification"
    data["dest"] = u_entry.get('name')
    return data


def msg_invalid_user(data, u_ip):
    data["msg"] = "User does not exist, closing client..."
    data["type"] = "wrong_user"
    data["dest"] = u_ip
    return data


def msg_invalid_password(data, u_name):
    data["msg"] = "User does not exist, closing client..."
    data["type"] = "wrong_user"
    data["dest"] = u_name
    return data
