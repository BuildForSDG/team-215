import os


class Config:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    ROOT_DIR = os.path.dirname(os.path.dirname(BASE_DIR))

    MONGODB_DB = "sanehutdb"
    MONGODB_HOST = "localhost"
    MONGODB_PORT = 27017
    MONGODB_USERNAME = ""
    MONGODB_PASSWORD = ""

    APP_PORT = 8000
    APP_HOST = "0.0.0.0"
    DEBUG = True
