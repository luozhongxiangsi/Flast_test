# encoding:utf-8
import pymysql
pymysql.install_as_MySQLdb()


USERNAME = 'root'
PASSWORD = 'lz1003!!'
HOST = '127.0.0.1'
PORT = 3306
DATABASES = 'db_demo1'
DB_URI = 'MySQL+pyMySQL://{}:{}@{}:{}/{}?charset=uft8'.format(USERNAME, PASSWORD, HOST, PORT, DATABASES)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True
