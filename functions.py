def useful_none():
    thing = None
    if thing:
        print("It's some thing")
    else:
        print("It's no thing")

    if thing is None:
        print("It's nothing")
    else:
        print("It's something")

    if not thing:
        print("thing(None) is not thing")

    thing = False
    if not thing:
        print("thing(False) is not thing")


def menu(wine, entree, dessert):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}


def buggy(arg, result=[]):
    result.append(arg)
    print(result)


def works(arg):
    result = []
    result.append(arg)
    return result


def nonbuggy(arg, result=None):
    if result is None:
        result = []
    result.append(arg)
    print(result)


def print_args(*args):
    print('Positional tuple:', args)


def print_more(required1, required2, *args):
    print('Need this one:', required1)
    print('Need this one. too:', required2)
    print('All the rest:', args)


if __name__ == '__main__':
    # useful_none()
    # print(menu('chardonnay', 'chicken', 'cake'))
    # print(menu('beef', 'bagel', 'bordeaux'))
    # print(menu(entree='beef', dessert='bagel', wine='bordeaux'))
    print_args(3, 2, 1, 'wait!', 'uh...')
    print_more('cap', 'gloves', 'scarf', 'monocle', 'mustache wax')
