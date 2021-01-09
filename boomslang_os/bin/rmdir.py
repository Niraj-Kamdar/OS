import os


def main(argv):
    paths = argv[1:]
    for path in paths:
        if not os.path.isdir(path):
            try:
                os.rmdir(path)
            except OSError:
                print(f"The directory is not empty: {path}")
        else:
            print(f"The directory {path} does not exists!")
    yield 0
