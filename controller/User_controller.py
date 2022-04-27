from models.User import User

class User_controller(object):

    def __init__(self, user: User):
        self.user = user
    
    def change_password(self, new_password):
        self.user.change_password(new_password)
    
    def change_role(self):
        self.user.change_role()