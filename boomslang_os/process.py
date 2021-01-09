import sys
from io import StringIO
from types import GeneratorType

from .system_call import SystemCall


class Process:
    process_id = 0

    def __init__(self, target, is_daemon):
        self.__class__.process_id += 1
        self.pid = self.__class__.process_id
        self.target = target
        self.send_value = None
        self.is_daemon = is_daemon
        self.stack = []

    def run(self):
        while True:
            try:
                result = self.target.send(self.send_value)
                if isinstance(result, SystemCall):
                    return result
                if isinstance(result, GeneratorType):
                    self.stack.append(self.target)
                    self.send_value = None
                    self.target = result
                else:
                    if not self.stack:
                        return
                    self.send_value = result
                    self.target = self.stack.pop()
            except StopIteration:
                if not self.stack:
                    raise
                self.send_value = None
                self.target = self.stack.pop()


class Daemon:
    def __enter__(self):
        self.f = StringIO()
        sys.stdout = self.f
        sys.stderr = self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stderr = sys.__stderr__
        sys.stdout = sys.__stdout__
        self.f.close()
