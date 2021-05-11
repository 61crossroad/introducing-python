def create_dict():
    empty_dict = {}

    bierce = {
        "day": "A period of twenty-four...",
        "positive": "Mistaken at",
        "misfortune": "The kind of fortune",
    }
    print(bierce)

    acme_customer = {'first': 'Wile', 'middle': 'E', 'last': 'Coyote'}
    print(acme_customer)
    acme_customer = dict(first="Wile", middle='E', last='Coyote')
    print(acme_customer)

    lol = [['a', 'b'], ['c', 'd'], ['e', 'f']]
    print(dict(lol))

    lot = [('a', 'b'), ('c', 'd'), ('e', 'f')]
    print(dict(lot))

    tol = (['a', 'b'], ['c', 'd'], ['e', 'f'])
    print(dict(tol))

    los = ['ab', 'cd', 'ef']
    print(dict(los))

    tos = ('ab', 'cd', 'ef')
    print(dict(tos))


def init_pythons():
    return {
        'Chapman': 'Graham',
        'Cleese': 'John',
        'Idle': 'Eric',
        'Jones': 'Terry',
        'Palin': 'Michael',
    }


def modify_dict():
    pythons = init_pythons()

    pythons['Gilliam'] = 'Gerry'
    pythons['Gilliam'] = 'Terry'


def access_dict():
    sp = init_pythons()
    print(sp['Idle'])

    print(sp.get('Groucho', 'Not a Python'))
    print(sp.get('Groucho'))

    print(sp.keys())  # iterator
    print(list(sp.keys()))  # list

    print(list(sp.values()))
    print(list(sp.items()))  # tuples in list
    print(len(sp))
