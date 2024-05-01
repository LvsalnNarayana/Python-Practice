import asyncio


async def main():
    print("Hello ...")
    await asyncio.sleep(1,result="waiting")
    print("... World!")


asyncio.run(main())
