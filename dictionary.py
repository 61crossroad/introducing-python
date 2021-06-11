import copy


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


def manipulation():
    first = {'a': 'agony', 'b': 'bliss'}
    second = {'b': 'bagels', 'c': 'candy'}
    concat = {**first, **second}
    print(type(concat))
    print(concat)

    third = {'d': 'donuts'}
    print({**first, **third, **second})

    pythons = init_pythons()
    print(pythons)
    others = {'Marx': 'Groucho', 'Howard': 'Moe'}
    pythons.update(others)
    print(pythons)

    first = {'a': 1, 'b': 2}
    second = {'b': 'platypus'}
    first.update(second)
    print(first)
    del pythons['Marx']
    print(pythons)
    print(pythons.pop('Palin'))
    print(pythons.pop('First', 'Hugo'))
    pythons.clear()
    print(pythons)


def assign_copy():
    signals = {'green': 'go',
               'yellow': 'go faster',
               'red': 'smile for the camera'}
    original_signals = signals.copy()
    signals['blue'] = 'confuse everyone'
    print(signals)
    print(original_signals)

    signals = {'green': 'go',
               'yellow': 'go faster',
               'red': ['stop', 'smile']}
    signals_copy = signals.copy()
    signals['red'][1] = 'sweat'
    print(signals_copy)

    signals = {'green': 'go',
               'yellow': 'go faster',
               'red': ['stop', 'smile']}
    signals_copy = copy.deepcopy(signals)
    signals['red'][1] = 'sweat'
    print(signals_copy)


def compare():
    a = {1: 1, 2: 2, 3: 3}
    b = {3: 3, 2: 2, 1: 1}
    print(a == b)
    a = {1: [1, 2], 2: [1], 3: [1]}
    b = {1: [1, 1], 2: [1], 3: [1]}
    print(a == b)


# def iteration():
