def mix_all():
    marx_list = ['Groucho', 'Chico', 'Harpo']
    marx_tuple = ('Groucho', 'Chico', 'Harpo')
    marx_dict = {'Groucho': 'banjo', 'Chico': 'piano', 'Harpo': 'harp'}
    marx_set = {'Groucho', 'Chico', 'Harpo'}

    print(marx_list[2])
    print(marx_tuple[2])
    print(marx_dict['Harpo'])


def combine():
    marxes = ['Groucho', 'Chico', 'Harpo']
    pythons = ['Chapman', 'Cleese', 'Gilliam', 'Jones', 'Palin']
    stooges = ['Moe', 'Curly', 'Larry']

    tuple_of_lists = marxes, pythons, stooges
    print(tuple_of_lists)

    list_of_lists = [marxes, pythons, stooges]
    print(list_of_lists)

    dict_of_lists = {'Marxes': marxes, 'Pythons': pythons, 'Stooges': stooges}
    print(dict_of_lists)

    houses = {
        (44.79, -93.14, 285): 'My House',
        (38.89, -77.03, 13): 'The White House'
    }
    print(houses)


if __name__ == '__main__':
    # mix_all()
    combine()
