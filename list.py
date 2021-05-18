def create_list():
    empty_list = []
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    first_names = ['Graham', 'John', 'Terry', 'Terry', 'Michael']
    leap_years = [2000, 2004, 2008]
    randomness = ['Punxsatawney', {"groundhog": "Phil"}, "Feb.2"]
    print(randomness)

    another_empty_list = list()

    print(list('cat'))
    a_tuple = ('ready', 'fire', 'aim')
    print(list(a_tuple))

    talk_like_a_pirate_day = '9/19/2019'
    print(talk_like_a_pirate_day.split('/'))

    splitme = 'a/b//c/d///e'
    print(splitme.split('/'))
    print(splitme.split('//'))


def init_marxes():
    return ['Groucho', 'Chico', 'Harpo']


def access_list():
    marxes = ['Groucho', 'Chico', 'Harpo']
    print(marxes[0], marxes[2])
    print(marxes[-1], marxes[-3])


def slice_list():
    marxes = ['Groucho', 'Chico', 'Harpo']

    print(marxes[0:2])  # 0, 1
    print(marxes[::2])  # 0, 2
    print(marxes[::-2])
    print(marxes[::-1])

    marxes.reverse()
    print(marxes)

    marxes.reverse()
    print(marxes[4:])
    print(marxes[-6:])  # -6 == 0 ->
    print(marxes[-6:-2])
    print(marxes[-6:-4])  # []


def modify_list():
    marxes = init_marxes()

    marxes.append('Zeppo')
    print(marxes)

    marxes.insert(2, 'Gummo(2)')
    print(marxes)
    marxes.insert(10, 'Zeppo(10)')
    print(marxes)

    print(["blah"] * 3)

    others = ['Gummo', 'Karl']
    marxes.extend(others)
    print(marxes)

    marxes += others
    print(marxes)

    marxes.append(others)
    print(marxes)

    marxes = init_marxes()
    marxes[2] = 'Wanda'
    print(marxes)


def init_numbers():
    return [1, 2, 3, 4]


def modify_list_by_slice():
    numbers = init_numbers()
    numbers[1:3] = [8, 9]
    print(numbers)

    numbers = init_numbers()
    numbers[1:3] = [7, 8, 9]
    print(numbers)

    numbers = init_numbers()
    numbers[1:3] = []
    print(numbers)

    numbers = init_numbers()
    huge = list()
    for i in range(11, 21):
        huge.append(i)
    numbers[1:3] = huge
    print(numbers)

    numbers = init_numbers()
    numbers[1:5] = init_numbers() * 3
    print(numbers)

    numbers = init_numbers()
    numbers[1:3] = 'wat?'
    print(numbers)


def delete_list():
    # ['Groucho', 'Chico', 'Harpo']
    marxes = init_marxes()
    marxes[len(marxes):] = ['Gummo', 'Karl']
    print(marxes)

    del marxes[-1]
    print('del marxes[-1]:', marxes)
    del marxes[1]
    print('del marxes[1]:', marxes)

    marxes = init_marxes()
    marxes.remove('Groucho')
    print(marxes)

    marxes = init_marxes()
    marxes.append('Zeppo')
    print(marxes)
    print(marxes.pop())
    marxes.pop(1)
    print(marxes)

    marxes.clear()
    print(marxes)

    marxes = init_marxes()
    marxes.append('Zeppo')
    print(marxes.index('Chico'))  # firstIndexOf

    print('Groucho' in marxes)
    print('Bob' in marxes)


def use_list():
    marxes = init_marxes()
    marxes.append('Zeppo')
    print(marxes.count('Harpo'))

    print(', '.join(marxes))

    friends = ['Harry', 'Hermione', 'Ron']
    separator = ' * '
    joined = separator.join(friends)
    print(joined)
    separated = joined.split(separator)
    print(separated)
    print('separated == joined ?', separated == friends)

    marxes = init_marxes()
    sorted_marxes = sorted(marxes)
    print(sorted_marxes)
    marxes.sort()
    print(marxes)
    numbers = [2, 1, 4.0, 3]
    numbers.sort(reverse=True)
    print(numbers)
    print(len(numbers))


def assign():
    a = [1, 2, 3]
    b = a
    a[0] = 'surprise'
    print(b)


def copies():
    a = [1, 2, 3]
    b = a.copy()
    c = list(a)
    d = a[:]
    a[0] = 'integer lists are boring'
    print(a)
    print(b)

    a = [1, 2, [8, 9]]
    b = a.copy()
    c = list(a)
    d = a[:]
    a[2][1] = 10
    print(a)
    print(d)

    print('## copy.deepcopy()')
    import copy
    a = [1, 2, [8, 9]]
    b = copy.deepcopy(a)
    a[2][1] = 10
    print(a)
    print(b)


def compare():
    a = [7, 2]
    b = [7, 2, 9]
    print(a == b)
    print(a <= b)
    print(a < b)
    a = [3, 2]
    b = [1, 2, 3]
    print(a > b)


def iteration():
    cheeses = ['brie', 'gjetost', 'havarti']
    for cheese in cheeses:
        print(cheese)

    for cheese in cheeses:
        if cheese.startswith('g'):
            print("I won't eat anything that starts with 'g'")
            break
        else:
            print(cheese)

    # cheeses.append('xavier')
    for cheese in cheeses:
        if cheese.startswith('x'):
            print("I won't eat anything that starts with 'x'")
            break
        else:
            print(cheese)
    else:
        print("Didn't find anything that started with 'x'")
