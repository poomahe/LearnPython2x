#constructor --> this is special function automatically called when object is created
#in this below program if we create 2objects its printing same name in both . so lets use constructor to which uses instance arguments.
class Person:
    name = "Amit"  #class /instance variable
    age = None

    def walk(self):
        a = 10 #local variable
        print("Hi! your name is ", self.name)
        print("Hi! your age is ", self.age)
        print(a)


amit = Person()
amit.walk()

poo = Person()
poo.walk()