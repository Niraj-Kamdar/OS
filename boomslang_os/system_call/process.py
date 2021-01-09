from . import SystemCall


class GetPid(SystemCall):

    def handle(self):
        self.process.send_value = self.process.pid
        self.scheduler.schedule(self.process)


class NewProcess(SystemCall):
    def __init__(self, target, is_daemon=False):
        self.target = target
        self.is_daemon = is_daemon

    def handle(self):
        pid = self.scheduler.new(self.target, self.is_daemon)
        self.process.send_value = pid
        self.scheduler.schedule(self.process)


class KillProcess(SystemCall):
    def __init__(self, pid):
        self.pid = pid

    def handle(self):
        process = self.scheduler.process_table.get(self.pid, None)
        if process:
            process.target.close()
            self.process.send_value = True
        else:
            self.process.send_value = False
        self.scheduler.schedule(self.process)


class WaitProcess(SystemCall):
    def __init__(self, pid):
        self.pid = pid

    def handle(self):
        result = self.scheduler.wait_for_exit(self.process, self.pid)
        self.process.send_value = result
        # if child process not exist in process table reschedule current process.
        if not result:
            self.scheduler.schedule(self.process)
