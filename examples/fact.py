def main(argv):
    def fact(num):
        if num == 1:
            yield 1
        else:
            yield num * (yield fact(num - 1))

    n = int(argv[1])
    result = yield fact(n)
    print(f"factorial({n}) = {result}")
    yield 0
