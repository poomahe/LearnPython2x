#Functions with argument
#Functions without arguments
#Functions with defecult values
#Functions with multiple arguments (*args and **kwargs)
#lambda

def say_hello():
    print("Hello")

say_hello()


def say_hello1(name):
    print(name)

say_hello1("poo")


def say_hello2(*args):
    for arg in args:
        print(arg)

say_hello2("poo", "Arasan")

a = lambda a: a ** 2
print(a(4))


def double_my_salary(salary):
    return salary*2

result = double_my_salary(10000)
print(result)

d_salary = lambda salary : salary * 2
print(d_salary(10000))