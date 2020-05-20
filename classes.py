# defining the class named Person
# it has 3 parameters that each instance of the class will need
# first name, last name, and age

class Person:
    def __init__(self, first, last, age):
        self.__first = first
        self.__last = last
        self.__age = age

    # declaring a public function that returns the full name of the instance of the class
    def getFullName(self):
        return self.__first + " " + self.__last

    def getAge(self):
        return self.__age

# creating an instance of the class
# we can do this as many times as we have people that we want to make a class instance for

p1 = Person("Jane", "Doe", 26)

# prints the full name of the individual

print(p1.getFullName())
print(p1.getAge())

try:
    print(p1.__first)
except:
    print("calling the __first variable failed")
