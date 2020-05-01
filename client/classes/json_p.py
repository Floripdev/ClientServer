import json


def format_data(data):
    data = json.dumps(data).encode('utf-8')
    return data


def deformat_data(data):
    data = json.loads(data.decode('utf-8'))
    return data
