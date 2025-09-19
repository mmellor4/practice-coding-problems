import asyncio


async def fn2():
    print("a pause in the system")


async def fn():
    print('This is ')
    await asyncio.sleep(1)
    await fn2()
    print('of asynchronous programming')
    await asyncio.sleep(1)
    print('and not multi-threading')

asyncio.run(fn())
