class Accounts():

    def __init__(self, id=0, username=None, password=None):
        self.id = id
        self.username = username
        self.password = password
        # self.conf_passw = conf_passw

    def getId(self):
        return self.id

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password

    # def getConfirmPassword(self):
    #     return self.conf_passw

    def setId(self, id):
        self.id = id

    def setUsername(self, username):
        self.username = username

    def setPassword(self, password):
        self.password = password

    # def setConfirmPassword(self, conf_passw):
    #     self.conf_passw=conf_passw

    def __str__(self) -> str:
        return ('{},{},{}'.format(self.id, self.username, self.password))
