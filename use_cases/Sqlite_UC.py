from controller.Sqlite_controller import Sqlite_controller
class Sqlite_UC(object):
    def __init__(self):
        self.sqlite_c = Sqlite_controller()

    def close_connection(self):
        self.sqlite_c.close_connection()

    def execute_query(self, query: str):
        self.sqlite_c.execute_query(query)
    
    def custom_search(self, dict: dict):
        self.sqlite_c.custom_search(dict)

    def insert_one(self, dict: dict):
        self.sqlite_c.insert_one(dict)

    def insert_multiples(self, list_of_dict:list):
        self.sqlite_c.insert_multiples(list_of_dict)

    def update(self, dict:dict):
        self.sqlite_c.update(dict)

    def delete(self, dict: dict):
        self.sqlite_c.delete(dict)

    def get_one(self, dict: dict):
        self.sqlite_c.get_one(dict)

    # def create_table(self, dict: dict):
        # self.sqlite_c.create_Table(dict)
