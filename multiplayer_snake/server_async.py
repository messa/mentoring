import asyncio

PORT = 50007              # Arbitrary non-privileged port

async def handle_echo(reader, writer):
    addr = writer.get_extra_info('peername')

    while True:
        data = await reader.read(100)
        if not data:
            break
        print(f"Received {data!r} from {addr!r}")

        await asyncio.sleep(3)

        reply = b'Odpoved: ' + data
        print(f"Send: {reply}")
        writer.write(reply)
        await writer.drain()

    print("Close the connection")
    writer.close()

async def main():
    server = await asyncio.start_server(handle_echo, '127.0.0.1', PORT)

    async with server:
        await server.serve_forever()

asyncio.run(main())
