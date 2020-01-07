import os

ENV_TYPE = os.environ.get('ENV_TYPE', '')
PRODUCTION_ENV = True if ENV_TYPE=='PRODUCTION' else False


DB_USER_NAME = "root" if PRODUCTION_ENV else "linkcool"
DB_USER_PW = "@ie0bzy3!dlpq*d7" if PRODUCTION_ENV else "forconnect"
DB_SEVER_ADDR = "10.0.1.4" if PRODUCTION_ENV else "119.145.69.74"
DB_SEVER_PORT = 4000 if PRODUCTION_ENV else 43021
DB_DATABASE_NAME = "bigdata"
'''
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{name:s}:{pw:s}@{addr:s}/{db:s}".format(
    name=DB_USER_NAME,
    pw=DB_USER_PW,
    addr=DB_SEVER_ADDR,
    db=DB_DATABASE_NAME)
'''
SQLALCHEMY_POOL_PRE_PING = True
SQLALCHEMY_ECHO = False if PRODUCTION_ENV else True
SQLALCHEMY_POOL_SIZE = 0
SQLALCHEMY_POOL_MAX_OVERFLOW = -1
SQLALCHEMY_POOL_RECYCLE = 120
