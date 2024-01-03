from werkzeug.security import generate_password_hash, check_password_hash

class User:
    def __init__(self, db, username, password,stocks=[]):
        self.db = db
        self.username = username
        self.password = password
        self.stocks = stocks

    def save_to_db(self):
        self.db.users.insert_one({'username': self.username, 'password': self.password,'stocks':self.stocks})

    @staticmethod
    def find_by_username(db, username):
        return db.users.find_one({'username': username})
    
    @staticmethod
    def find_by_username2(db, username):
        return User(db,username,User.find_by_username(db,username)['password'],User.find_by_username(db,username)['stocks'])
        
    
    def add_stock(self,stock):
        self.stocks.append(stock)
        self.db.users.update_one({'username':self.username},{'$set':{'stocks':self.stocks}})

    def remove_stock(self,stock):
        self.stocks.remove(stock)
        self.db.users.update_one({'username':self.username},{'$set':{'stocks':self.stocks}})
    
    def get_stocks(self):
        return self.stocks
    
    def get_username(self):
        return self.username
    
    def get_password(self):
        return self.password
    
    def update_stock(self,stock_list):
        self.stocks = stock_list
        self.db.users.update_one({'username':self.username},{'$set':{'stocks':stock_list}})
        return True
    
    def add_stock(self,stock):
        self.stocks.append(stock)
        self.db.users.update_one({'username':self.username},{'$set':{'stocks':self.stocks}})
        return True
    
    def remove_stock(self,stock):
        self.stocks.remove(stock)
        self.db.users.update_one({'username':self.username},{'$set':{'stocks':self.stocks}})
        return True

    @staticmethod
    def hash_password(password):
        return generate_password_hash(password, method='sha256')

    @staticmethod
    def check_password(hashed_password, password):
        return check_password_hash(hashed_password, password)
