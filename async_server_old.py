import socket, asyncio


async def set_connection(client):
    loop = asyncio.get_event_loop()
    request = None
    with client:
        while request != 'quit':
            request = (await loop.sock_recv(client, 1024)).decode('utf8')
            await loop.sock_sendall(client, request.encode('utf8'))


async def run_server():
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.bind(('localhost', 5556))
    connection.listen(10)
    connection.setblocking(False)

    loop = asyncio.get_event_loop()

    while True:
        client, addr = await loop.sock_accept(connection)
        loop.create_task(set_connection(client))


asyncio.run(run_server())
