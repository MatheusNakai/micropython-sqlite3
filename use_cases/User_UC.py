from controller.User_controller import User_controller

class User_Uc(object):
    
    def __init__(self, user_controller: User_controller):
        self.user_c = user_controller

    def change_password(self, new_password:str):
        self.user_c.change_password(new_password)

    def change_role(self):
        self.user_c.change_role()
    
