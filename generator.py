def get_natural_number():
    n = 0
    while True:
        n += 1
        yield n


def generator():
    yield 1
    yield 'string'
    yield True

# TODO range with lsit
# def range():

# TODO enumerate throws TypeError
# def enumerate():
    # a = [1, 2, 3, 2, 45, 2, 5]
    # print(a
# )
