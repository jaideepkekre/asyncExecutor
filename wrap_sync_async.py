import asyncio
import requests
import math
def sync_work(num):

    return math.pow(num,2)



async def main():
    loop = asyncio.get_event_loop()
    future1 = loop.run_in_executor(None, sync_work, 55)
    future2 = loop.run_in_executor(None, sync_work, 57)
    response1 = await future1
    response2 = await future2
    print(response1)
    print(response2)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
