from aiohttp.web import middleware

@middleware
async def db_middleware(request, handler):
    engine = request.app['db_engine']
    async with engine.acquire() as conn:
        request['db_connection'] = conn
        return await handler(request)
