import aiohttp
import asyncio
import time
from asyncio_enabler import asyncExecutor


resp = list()


async def work(session, url, id):
    async with session.get(url) as response:
        if id == 1:
            await asyncio.sleep(10)
        js = await response.json()
        resp.append(js)
        print(id)


async def runner(url, id):
    async with aiohttp.ClientSession() as session:
        await work(session, url, id)


asyncExe = asyncExecutor()

asyncExe.addtask(runner('https://jsonplaceholder.typicode.com/posts/1', 1))
asyncExe.addtask(runner('https://jsonplaceholder.typicode.com/posts/1', 2))
asyncExe.addtask(runner('https://jsonplaceholder.typicode.com/posts/1', 3))

asyncExe.run()
