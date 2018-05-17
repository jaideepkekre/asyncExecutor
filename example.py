import aiohttp
import asyncio
import time
from asyncio_enabler import asyncExecutor


resp = list()


async def work(session, url, uid):
    async with session.get(url) as response:
        if uid == 1:
            await asyncio.sleep(10)
        js = await response.json()
        resp.append(js)
        print(uid)


async def runner(url, uid):
    async with aiohttp.ClientSession() as session:
        await work(session, url, uid)


asyncExe = asyncExecutor()

asyncExe.addtask(runner('https://jsonplaceholder.typicode.com/posts/1', 1))
asyncExe.addtask(runner('https://jsonplaceholder.typicode.com/posts/1', 2))
asyncExe.addtask(runner('https://jsonplaceholder.typicode.com/posts/1', 3))

asyncExe.run()
