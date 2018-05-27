class Config(object):
    DEBUG = False


    SQLALCHEMY_DATABASE_URI='mysql://root@localhost:3306/xjzx'
    SQLALCHEMY_TRACK_MODIFICATIONS=True


class DevelopConfig(Config):
    DEBUG = True
