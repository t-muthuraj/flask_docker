import os

DB_USER = os.environ.get('USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('HOST')
DB_NAME = os.environ.get('DATABASE')

DATABASE_CONNECTION_URI = "mysql+pymysql://{}:{}@{}/{}".format(DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)