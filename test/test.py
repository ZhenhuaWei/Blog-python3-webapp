import orm
import asyncio
from models import User, Blog, Comment

async def test(loop):
    yield from orm.create_pool(loop=loop,user='root', password='password', database='python')

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    yield from u.save()

if name == 'main':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
    loop.run_forever()


    