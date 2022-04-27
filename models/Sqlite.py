import sqlite3

class Sqlite(object):
    def __init__(self):
        self.db = None
        self.create_connection()

    def create_connection(self):
        try:
            self.db = sqlite3.connect("database.db")
        except sqlite3.Error as err:
            print(err)

    def close_connection(self):
        self.db.close()

    def execute_query(self, query: str):
        cursor = self.db.cursor()
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except sqlite3.Error as err:
            print(err)
            return None

    def custom_search(self,dictionary: dict):
        table = dictionary["table"]
        column = dictionary["column"]
        where = dictionary["where"]
        result = self.execute_query(f"SELECT {column} FROM {table} WHERE {where}")
        if result is not None:
            for row in result:
                print(row)
            return result
        else:
            return None

    def insert_one(self,dictionary: dict):
        table = dictionary.pop("table")
        keys = ""
        values = ""
        for key, value in dictionary.items():
            keys += f"{key},"
            values += f"'{value}',"
        keys = keys[:-1]
        values = values[:-1]
        query = f"INSERT INTO {table} ({keys}) VALUES ({values})"
        self.execute_query(query)

    def insert_multiples(self,list_of_dict: list):
        for dicti in list_of_dict:
            self.insert_one(dicti)

    def update(self, dictionary: dict):
        id = dictionary["id"]
        table = dictionary.pop("table")
        query = f"UPDATE {table} SET "
        for key, value in dictionary.items():
            query += f"{key}='{value}',"
        query = query[:-1]
        query += f" WHERE id={id}"
        self.execute_query(query)
        self.db.commit()

    def delete(self,dictionary: dict):
        table = dictionary["table"]
        condition = dictionary["condition"]
        query = f"DELETE FROM {table} WHERE {condition}"
        self.execute_query(query)
        self.db.commit()
    
    def get_one(self, dictionary: dict):
        result = self.custom_search(dictionary)
        if result is not None:
            return result[0]

    def get_multiple(self, dictionary: dict):
        list_Of_Dictionary = []
        result = self.custom_search(dictionary)
        if result is not None:
            for row in result:
                list_Of_Dictionary.append(row)
                self.close_connection()
            return list_Of_Dictionary
        else:
            print("tabela vazia")



    # def create_Table(self, dictionary: dict):
    #     table = dictionary["table"]
    #     query = f"CREATE TABLE {table} ("
    #     for key, value in dictionary.items():
    #         if type(value) is int or bool:
    #             data_type = "INTEGER"
    #         if type(value) is str:
    #             data_type = "TEXT"

    #         query += f"{key} {data_type},"
    #     query = query[:-1]
    #     query += ")"
    #     print(query)
    #     self.execute_query(query)
        
sqlite= Sqlite()
a={
    "row": "*",
    "table": "users",
    "where": "id>0"
}
print(a.pop("table"))
print(a)
#sqlite.insert_one(a)