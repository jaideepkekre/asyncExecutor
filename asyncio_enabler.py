import asyncio
import logging


class asyncExecutor:

    def __init__(self):
        self.tasklist = list()
        try:
            self.loop = self._get_event_loop()
        except:
            self.loop=asyncio.new_event_loop()
            asyncio.set_event_loop(self.loop)
        self.used=False
       

    def _get_event_loop(self):
        return asyncio.get_event_loop()

    def addtask(self,func):
        if self.used:
            raise RuntimeError(
                "This executor has been used!\nPlease instantiate a new one")

        self.tasklist.append(self.loop.create_task(func))

    def run(self):
        if self.used :
            raise RuntimeError(
                "This executor has been used!\nPlease instantiate a new one")
        wait_tasks = asyncio.wait(self.tasklist)
        self.loop.run_until_complete(wait_tasks)
        # self.loop.close()
        self.used = True
