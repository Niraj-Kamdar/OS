import select
from collections import defaultdict
from queue import Queue

from .process import Process, Daemon
from .system_call import SystemCall


class Scheduler:
    def __init__(self):
        self.ready_queue = Queue()
        self.process_table = {}

        # Tasks waiting for other tasks to exit
        self.exit_wait = defaultdict(list)
        self.read_wait = {}
        self.write_wait = {}

    def new(self, target, is_daemon=False):
        new_process = Process(target, is_daemon)
        self.process_table[new_process.pid] = new_process
        self.schedule(new_process)
        return new_process.pid

    def exit(self, process):
        del self.process_table[process.pid]
        for process in self.exit_wait.pop(process.pid, []):
            self.schedule(process)

    def wait_for_exit(self, process, pid):
        if pid in self.process_table:
            self.exit_wait[pid].append(process)
            return True
        else:
            return False

    def wait_for_read(self, process, fd):
        self.read_wait[fd] = process

    def wait_for_write(self, process, fd):
        self.write_wait[fd] = process

    def io_poll(self, timeout):
        if self.read_wait or self.write_wait:
            r, w, e = select.select(self.read_wait, self.write_wait, [], timeout)
            for fd in r:
                self.schedule(self.read_wait.pop(fd))
            for fd in w:
                self.schedule(self.write_wait.pop(fd))

    def io_run(self):
        while True:
            self.io_poll(0)
            yield

    def schedule(self, process):
        self.ready_queue.put(process)

    def mainloop(self):
        self.new(self.io_run())
        while self.process_table:
            process = self.ready_queue.get()
            try:
                if process.is_daemon:
                    result = process.run()
                else:
                    result = process.run()
                if isinstance(result, SystemCall):
                    result.process = process
                    result.scheduler = self
                    result.handle()
                    continue
            except StopIteration:
                self.exit(process)
                continue
            self.schedule(process)
