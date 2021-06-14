def create():
    empty_set = set()
    print(empty_set)

    even_numbers = {0, 2, 4, 6, 8}
    print(even_numbers)
    print(type(even_numbers))

    dict_to_set = set({'apple': 'red', 'orange': 'orange', 'cherry': 'red'})
    print(dict_to_set)
    print(type(dict_to_set))


def membership():
    drinks = {
        'martini': {'vodka', 'vermouth'},
        'black russian': {'vodka', 'kahlua'},
        'white russian': {'cream', 'kahlua', 'vodka'},
        'manhattan': {'rye', 'vermouth', 'bitters'},
        'screwdriver': {'orange juice', 'vodka'}
    }

    print('[vodka]')
    for name, contents in drinks.items():
        if 'vodka' in contents:
            print(name)

    print('[vodka & ^(vermouth & cream)]')
    for name, contents in drinks.items():
        if 'vodka' in contents and not ('vermouth' in contents or 'cream' in contents):
            print(name)


def combination_operator():
    drinks = {
        'martini': {'vodka', 'vermouth'},
        'black russian': {'vodka', 'kahlua'},
        'white russian': {'cream', 'kahlua', 'vodka'},
        'manhattan': {'rye', 'vermouth', 'bitters'},
        'screwdriver': {'orange juice', 'vodka'}
    }

    for name, contents in drinks.items():
        if contents & {'vermouth', 'orange juice'}:
            print(name)

    for name, contents in drinks.items():
        if 'vodka' in contents and not contents & {'vermouth', 'cream'}:
            print(name)

    bruss = drinks['black russian']
    wruss = drinks['white russian']
    print(bruss & wruss)
    print(bruss | wruss)
    print('[difference]')
    print(bruss - wruss)
    print(wruss - bruss)
    print(bruss <= wruss)
    print(bruss < wruss)

    a = {1, 2}
    b = {2, 3}

    print(a & b)
    print(a.intersection(b))

    print(a | b)
    print(a.union(b))

    print(a - b)
    print(a.difference(b))

    print(a ^ b)
    print(a.symmetric_difference(b))

    print(a <= b)
    print(a.issubset(b))


def comprehension():
    a_set = {number for number in range(1, 6) if number % 3 == 1}
    print(a_set)


def immutable_set():
    print(frozenset([3, 2, 1]))
    print(frozenset({2, 1, 3}))
    fs = frozenset([3, 2, 1])
    print(fs)
    # fs.add(4)


if __name__ == '__main__':
    # create()
    # membership()
    # combination_operator()
    # comprehension()
    immutable_set()
