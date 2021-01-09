import os


def main(argv):
    if len(argv) < 2:
        print("Insufficient Arguments!")
    else:
        path = argv[1]
        if os.path.exists(path):
            os.chdir(path)
        else:
            print(f"Invalid path: {path}")
    yield 0
