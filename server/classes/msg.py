from .protocol import net_protocol


def msg_welcome(s_entry, u_entry):
    data = net_protocol
    data["msg"] = f"Welcome to the {s_entry.get('name')} {u_entry.get('name')}! :) connected to {s_entry.get('ip')} on Port: {s_entry.get('port')}"
    data["type"] = "notification"
    data["dest"] = u_entry.get('name')
    return data


def msg_invalid_user(data):
    data["msg"] = "User does not exist, closing client..."
    data["type"] = "wrong_user"
    data["dest"] = data['src']
    return data


def msg_invalid_password(data):
    data["msg"] = "Password does not exist, closing client..."
    data["type"] = "wrong_user"
    data["dest"] = data['user']
    return data
