from aiohttp import web
from sqlalchemy.sql import select, and_, bindparam
from models.models import ebay_analysis_user

routes = web.RouteTableDef()


@routes.get('/')
async def hello(request):
    return web.Response(text="Hello, world")


@routes.post('/api_v1/register')
async def relationship(request):
    connection = request['db_connection']

    # 获取参数
    data = await request.post()
    if data:
        name = data['name']
        phone = data['phone']
        password = data['password']
        sms_code = data['sms_code']
        validate_code = data['validate_code']

        # 校验参数
        # 校验name

        # 校验phone
        # 校验password
        # 校验sms_code
        # 校验validate_code
        cursor = await connection.execute(ebay_analysis_user.select())
        records = await cursor.fetchall()

        return web.Response(text=str())
