# coding:utf-8
DB_USER = 'root'
DB_PASSEORD = 'root'
DB_HOST = 'localhost'
DB_DB = 'test'

DEBUG = True
PORT = 3333
HOST = '0.0.0.0'
SECRET_KEY = 'my gwt'

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'mysql://'+ DB_USER +':' +DB_PASSEORD + '@' + DB_HOST + '/' + DB_DB