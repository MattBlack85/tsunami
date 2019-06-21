import asyncio
from multiprocessing import Process

import aiohttp


class Tsunami(Process):

    def __init__(self, url, n_req):
        self.url = url
        self.n_req = n_req
        super().__init__()

    async def execute(self):
        async with aiohttp.ClientSession() as session:
            tasks = [
                asyncio.create_task(
                    self.send_request(session, self.url)
                ) for _ in range(self.n_req)
            ]
            start = asyncio.get_event_loop().time()
            await asyncio.gather(*tasks)
            end = asyncio.get_event_loop().time()
            print(f'Done {self.n_req} requests in {end - start}')

    async def send_request(self, session, url):
        try:
            async with session.get(url) as resp:
                await resp.text()
        except aiohttp.client_exceptions.ClientError:
            pass

    def run(self):
        asyncio.run(self.execute())
