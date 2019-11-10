import asyncio

HOST = 'localhost'
PORT = 9096


async def handle_echo(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    print(message)

    writer.write(data)
    await writer.drain()

    writer.close()


async def main(HOST, PORT):
    server = await asyncio.start_server(handle_echo, HOST, PORT)
    await server.serve_forever()



# Close the server
asyncio.run(main(HOST, PORT))