from models.Sqlite import Sqlite

class Sqlite_controller(object):
    
    def __init__(self):
        self.sqlite = Sqlite()

    def close_connection(self):
        self.sqlite.close_connection()

    def execute_query(self, query: str):
        self.sqlite.execute_query(query)
    
    def custom_search(self, dict: dict):
        self.sqlite.custom_search(dict)

    def insert_one(self, dict: dict):
        self.sqlite.insert_one(dict)

    def insert_multiples(self, list_of_dict:list):
        self.sqlite.insert_multiples(list_of_dict)

    def update(self, dict:dict):
        self.sqlite.update(dict)

    def delete(self, dict: dict):
        self.sqlite.delete(dict)

    def get_one(self, dict: dict):
        self.sqlite.get_one(dict)

    # def create_table(self, dict: dict):
        # self.sqlite.create_Table(dict)

