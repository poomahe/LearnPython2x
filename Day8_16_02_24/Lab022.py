#map & Filter
# MAP (iterate each & every element)
# this function often used when you need to transform each element is iterable using specific function& collect the results

# Filter --> Filter the items from the list based on the logic
# return less number of items

#map function example
def double(num):
    return num * 2

my_list = [1,2.3]
result = list(map(double,my_list))
print(result)

#Filter example

numbers = [1 , 2, 3, 4]
even_number = tuple(filter(lambda x: x%2==0, numbers))
print(even_number)

#Dont use lambda always, juniors will get confuse to understand the logic


def my_func(num):
    return num%2==0

numbers = [1 , 2, 3, 4]
even_number = tuple(filter(my_func,numbers))
print(even_number)