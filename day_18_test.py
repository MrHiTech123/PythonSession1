def do_thing_to_1(thing):
    return thing(1)

def add_two(a):
    return a + 2

print(do_thing_to_1(add_two))
(do_thing_to_1(print))



