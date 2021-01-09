from . import SystemCall


class ReadWait(SystemCall):
    def __init__(self, f):
        self.f = f

    def handle(self):
        fd = self.f.fileno()
        self.scheduler.wait_for_read(self.process, fd)


class WriteWait(SystemCall):
    def __init__(self, f):
        self.f = f

    def handle(self):
        fd = self.f.fileno()
        self.scheduler.wait_for_write(self.process, fd)


class Socket(object):
    def __init__(self, sock):
        self.sock = sock

    def accept(self):
        yield ReadWait(self.sock)
        client, addr = self.sock.accept()
        yield Socket(client), addr

    def send(self, buffer):
        while buffer:
            yield WriteWait(self.sock)
            length = self.sock.send(buffer)
            buffer = buffer[length:]

    def recv(self, max_bytes):
        yield ReadWait(self.sock)
        yield self.sock.recv(max_bytes)

    def close(self):
        yield self.sock.close()
