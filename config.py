import os
class Config:
    SECRET_KEY = os.environ.get('d172824e973e59cfa6c8bf70fbc8992e') or 'mysecretkey'
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'rahul'
    MYSQL_PASSWORD = 'Xh4dJ-J+'
    MYSQL_DB = 'customerpanelapp'
