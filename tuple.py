def create_tuple():
    empty_tuple = ()
    print(empty_tuple)

    one_marx = 'Groucho',  # tuple
    print(one_marx)
    one_marx = ('Groucho',)  # tuple
    print(one_marx)
    one_marx = ('Grouch')  # str
    print(type(one_marx))

    marx_tuple = 'Groucho', 'Chico', 'Harpo'
    print(marx_tuple)

    one_marx = 'Groucho',
    print(type(one_marx))  # tuple
    print(type('Groucho',))  # str
    print(type(('Groucho',)))  # tuple

    marx_tuple = ('Groucho', 'Chico', 'Harpo')
    a, b, c = marx_tuple
    print(a)
    print(b)
    print(c)

    password = 'swordfish'
    icecream = 'tuttifrutti'
    password, icecream = icecream, password
    print(password, type(password))


def use_tuple():
    marx_list = ['Groucho', 'Chico', 'Harpo']
    print(tuple(marx_list))

    print(('Groucho',) + ('Chico', 'Harpo'))
    print(('yada',) * 3)

    a = (7, 2,)
    b = (7, 2, 9,)
    print('a: ', a)
    print('b: ', b)
    print('a == b ? ', a == b)
    print('a <= b ? ', a <= b)
    print('a < b ? ', a < b)

    words = ('fresh', 'out', 'of', 'ideas')
    for word in words:
        print(word)

    t1 = ('Fee', 'Fie', 'Foe')
    t2 = 'Flop',
    print(type(t2))  # tuple
    print(type('Flop',))  # str
    print(t1 + t2)

    print(id(t1))
    t1 += t2
    print(id(t1))
