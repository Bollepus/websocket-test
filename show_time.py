#!/usr/bin/env python
import asyncio
import datetime
import random
import websockets
 
async def show_time(websocket):
     while True:
        message = datetime.datetime.utcnow().isoformat() + "Z"
        await websocket.send(message)
        await asyncio.sleep(random.random() * 2 + 1)

async def main():
    async with websockets.serve(show_time, "10.2.0.4", 5678):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())