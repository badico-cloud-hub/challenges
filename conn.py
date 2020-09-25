import redis
from pymongo import MongoClient
from challenge_b import app

# get mongodb conn data
m_uri, m_port = app.config['MONGODB_CONN'] 

class ConnMongo:
    
    def __init__(self, db):
        
        self.__c = MongoClient(m_uri, m_port)
        self.__db = self.__c[db]
    
    @property    
    def get_db(self):
        return self.__db
        
    @property
    def server_info(self):
        return self.__c.server_info()

class ConnRedis:
    def __init__(self):
        self.r = redis.Redis(host='localhost', port=6379, db=0)
    
    def conn(self):
            return self.r
    
    def testConn(self):
        self.r.set('foo', 'bar')
        return self.r.get('foo')

    # def setR(self, key, value):
    #     self.r.set(key, value)
    
    # def getR(self, key):
    #     return self.r.get(key)

# create conn tests
if __name__ == '__main__':
    m = ConnMongo('challenge_b')
    # print(m.server_info)
    print(m.get_db)
    