def add_two_nums(num_1, num_2=0):
    return num_1 + num_2

def subtract_two_nums(num_1, num_2=3):
    return num_1 - num_2

print(subtract_two_nums(2, 1))
print(subtract_two_nums(4))

def print_all(*stuff_to_print, every_time):
    for i in stuff_to_print:
        print(i, every_time)

print_all(2, 45, 6, 'hello', every_time='this')





