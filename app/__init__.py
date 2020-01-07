from aiohttp import web
from config import *
from app.auth import views
# from sqlalchemy import create_engine
from aiomysql.sa import create_engine
from .middleware import db_middleware

app = web.Application(middlewares=[db_middleware])


async def init_db(app):
    app['db_engine'] = await create_engine(
        # pool_pre_ping=SQLALCHEMY_POOL_PRE_PING,
        echo=SQLALCHEMY_ECHO,
        # pool_size=SQLALCHEMY_POOL_SIZE,
        # max_overflow=SQLALCHEMY_POOL_MAX_OVERFLOW,
        pool_recycle=SQLALCHEMY_POOL_RECYCLE,
        autocommit=True,
        user=DB_USER_NAME, db=DB_DATABASE_NAME,
        host=DB_SEVER_ADDR, port=DB_SEVER_PORT, password=DB_USER_PW,
        maxsize=10
    )
    print("连接成功")


async def close_db(app):
    app['db_engine'].close()
    await app['db_engine'].wait_closed()


app.on_startup.append(init_db)
app.on_cleanup.append(close_db)

'''
app['db_engine'] = create_engine(
    SQLALCHEMY_DATABASE_URI,
    pool_pre_ping=SQLALCHEMY_POOL_PRE_PING,
    echo=SQLALCHEMY_ECHO,
    pool_size=SQLALCHEMY_POOL_SIZE,
    max_overflow=SQLALCHEMY_POOL_MAX_OVERFLOW,
    pool_recycle=SQLALCHEMY_POOL_RECYCLE,
)
'''

app.add_routes(auth.views.routes)
