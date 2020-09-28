from conn import ConnMongo

class Model:
    def __init__(self, db:str, col:str):
        self._conn = ConnMongo(db)
        self._col = self.__set_col(col)
    
    def __set_col(self, col):
        return self._conn.get_db[col]

    def get_db(self):
        return self._conn.get_db

    @property
    def collection(self):
        return self._col
    
    # define blueprint
    def create(self, content:dict):
        self.collection.insert_one(content)

    def find(self, content):
        return self.collection.find_one(content)
    def delete(self):pass
    def update(self):pass

class UserModel(Model):
    def __init__(self):
        super().__init__('challenge_b', 'users')
        
user_model = UserModel()

class GeocodingModel(Model):
    def __init__(self):
        super().__init__('challenge_b', 'geocoding')

geo_model = GeocodingModel()


if __name__ == "__main__":
    pass
    