name = 'batman'
print(len(name))
print(name[0])
print(len(name)-1)
print(name[len(name)-1])

#string immutable (can't be change/modify)
string = 'poo'
string = 'arasan'
print(string)
string[0] = 'p' #TypeError: 'str' object does not support item assignment