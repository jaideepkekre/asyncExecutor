import aiohttp
import time
from asyncio_enabler import asyncExecutor
from flask import Flask, render_template, make_response, request, Response


resp = list()


async def work(session, url, uid):
    async with session.get(url) as response:        
        js = await response.json()
        resp.append(js)
        print(uid)


async def runner(url, uid):
    async with aiohttp.ClientSession() as session:
        await work(session, url, uid)


# asyncExe = asyncExecutor()

# asyncExe.addtask(runner('https://jsonplaceholder.typicode.com/posts/1', 1))
# asyncExe.addtask(runner('https://jsonplaceholder.typicode.com/posts/1', 2))
# asyncExe.addtask(runner('https://jsonplaceholder.typicode.com/posts/1', 3))

# asyncExe.run()


app = Flask(__name__)

# Modification 2: Define your own Flask app routes and functions


@app.route('/')
def index():
    asyncExe = asyncExecutor()
    asyncExe.addtask(runner('https://jsonplaceholder.typicode.com/posts/1', 1))
    asyncExe.addtask(runner('https://jsonplaceholder.typicode.com/posts/1', 2))
    asyncExe.addtask(runner('https://jsonplaceholder.typicode.com/posts/1', 3))
    asyncExe.run()
    return ("mew")
