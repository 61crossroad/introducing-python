thing = 'woodchuck'
print('{}'.format(thing))
place = 'lake'
print('The {} is in the {}.'.format(thing, place))
print('The {1} is in the {0}.'.format(place, thing))
print('The {thing} is in the {place}.'.format(thing='duck', place='bathtub'))

d = {'thing': 'duck', 'place': 'bathtub'}
print('The {0[thing]} is in the {0[place]}.'.format(d))

thing = 'Wraith'
place = 'window'
print('\'The {} is at the {}\''.format(thing, place))
print('\'The {:10s} is at the {:10s}\''.format(thing, place))
print('\'The {:<10s} is at the {:<10s}\''.format(thing, place))
print('\'The {:^10s} is at the {:^10s}\''.format(thing, place))
print('\'The {:>10s} is at the {:>10s}\''.format(thing, place))
print('\'The {:!^10s} is at the {:!^10s}\''.format(thing, place))

thing = 'wereduck'
place = 'werepond'
print(f'\'The {thing} is in the {place}\'')
print(f'\'The {thing:>20} is in the {place:.^20}\'')
print(f'\'{thing =}, {place =}\'')
print(f'\'{thing[-4:] =}, {place.title() =}\'')
print(f'{thing = :>4.4}')
