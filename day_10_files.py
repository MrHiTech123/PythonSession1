
f = open('my_file.txt', 'w')
# 3 modes:
#  w = writing
#  a = appending
#  r = reading

f.write('Hello file system skibidi\n')
f.write('Hello skibidi is very very unpoggers\n')
f.write('\tI do not grok skibidi\n')

f.close()



f = open('my_file.txt', 'r')

# text = f.read()
# 
# print(text)
# print(text.split('s'))



for line in f:
    print(line[:-1])


