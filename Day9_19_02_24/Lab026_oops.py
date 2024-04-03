#class --> its a blue print & contains data members(Attributes) & methods(Behavior) .. Class creation will not store any memory

#objects --> instance of class .. All data members (attributes ) & member funcations (behaviors) of the class can be access using objects
      #objects are allocated memory spaces


#object - classname(0

class Car:
    name = None   #class variable or Instance variable
    colour = None
    model = None
    speed = None
    engine = None

    def start_engine(self):
        a=10 #local variable
        print("Start Engine")

    def drive(self):
        print("drive")

    def car_break(self):
        print("Break")

    def who_is_driving(self):
        print("I'm driving --> " +self.name)

tesla = Car()
lambor = Car()

tesla.name = "Tesla"
lambor.name = "Lamborghini"

tesla.who_is_driving()
lambor.who_is_driving()


