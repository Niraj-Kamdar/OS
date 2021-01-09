import os


def main(argv):
    paths = argv[1:]
    for path in paths:
        if not os.path.isdir(path):
            os.mkdir(path)
        else:
            print(f"{path} Already exists!")
    yield 0