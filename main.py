class User:
    def __init__(selfself, id, name, user=True):
        self.id = id
        self.name = name
        self.user = user




class Admin(User):
    def __init__(self, id, name, user, admin=True):
        super().__init__(id, name, user)
        self.admin = admin