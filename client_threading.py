import socket, threading


def handle_messages(connection: socket.socket):
    while True:
        try:
            msg = connection.recv(1024)
            if msg:
                print(msg.decode())
            else:
                connection.close()
                break

        except Exception as e:
            print(f'Error handling message from server: {e}')
            connection.close()
            break


def client() -> None:
    try:
        connection = socket.socket()
        connection.connect(("localhost", 5555))
        threading.Thread(target=handle_messages, args=[connection]).start()

        print('Connected to chat!')

        while True:
            msg = input()

            if msg == 'quit':
                break

            connection.send(msg.encode())

        connection.close()

    except Exception as e:
        print(f'Error connecting to server socket {e}')
        connection.close()


if __name__ == "__main__":
    client()
