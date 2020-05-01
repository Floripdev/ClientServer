class user:
    def __init__(self, uname, ids, host):
        self.username = uname
        self.idenitfier = ids
        self.ip = host

    def getName(self):
        return self.username

    def getId(self):
        return self.idenitfier

    def getIp(self):
        return self.ip
