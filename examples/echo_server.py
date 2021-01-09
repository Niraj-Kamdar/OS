from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR

from boomslang_os.system_call.process import NewProcess
from boomslang_os.system_call.socket import Socket


def main(argv):
    def handle_client(client, addr):
        print("Connection from", addr)
        while True:
            data = yield client.recv(65536)
            if not data:
                break
            yield client.send(data)
        print("Client closed")
        yield client.close()

    print("Server starting")
    rawsock = socket(AF_INET, SOCK_STREAM)
    rawsock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    rawsock.bind(("", 5000))
    rawsock.listen(1024)

    sock = Socket(rawsock)
    while True:
        yield None
        client, addr = yield sock.accept()
        yield NewProcess(handle_client(client, addr))
