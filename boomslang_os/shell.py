import importlib

from .system_call.process import NewProcess, WaitProcess


def main():
    while True:
        yield None
        command_string = input("sh$ ").strip()
        if not command_string:
            continue
        argv = command_string.split()
        cmd = argv[0]
        if cmd == "echo":
            print(*argv[1:])
        elif cmd == "exit":
            return
        else:
            try:
                command = importlib.import_module(cmd)
                if getattr(command, "main"):
                    # child = yield command.main(argv)
                    child = yield NewProcess(command.main(argv))
                    if argv[-1] != "&":
                        yield WaitProcess(child)
                else:
                    print(f"Invalid command: {command_string}")
            except ImportError:
                print(f"Invalid command: {command_string}")

