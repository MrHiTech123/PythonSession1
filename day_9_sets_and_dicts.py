# sets and dicts

l = [1, 2, 4, 12, 12]

s = {1, 4, 2, 12, 12}

d = {
    1: 'skibidi',
    'hot diggity': 'dog'
}

print(d['hot diggity'])


player = {
    'strength': 10,
    'rizz': 12,
    'armor': 20,
    'health': 0,
    'wealth': 100,
    'wisdom': 'skibidi toilet'
}

print(player['strength'] + player['rizz'] + player['armor'] + player["health"] + player['wealth'])

nested_dict = {
    'fluid': {
        'fluid_name': 'water',
        'amount': 100
    }
}

print(nested_dict['fluid']['amount'])


s = 'This is a string' + ' yes it is'

print(s)

l = [1, 2, 3]

def append_one(l):
    l.append(1)
def add_one(s):
    s += '1'

append_one(l)

s = '2345'
add_one(s)
print(s)
import os

os.system('cls')





