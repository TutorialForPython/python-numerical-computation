import asyncio
from dask.distributed import Client
loop = asyncio.get_event_loop()

def square(x):
    return x ** 2

async def test1():
    client = Client('localhost:8786')
    A = client.map(square, range(10000))
    f = client.submit(sum, A)
    result = await client.gather(f,asynchronous=True)
    print(result)
    return result

loop.run_until_complete(test1())
