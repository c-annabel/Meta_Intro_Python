#Encapsulation
class Alpha:

    def __init__(self):
        self._a = 2.  # Protected member ‘a’, 1 underscore, can be accessed by the class and its subclasses.
        self.__b = 2.  # Private member ‘b’, 2 underscores, an only be accessed from within the class Alpha.

#Polymorphism
#it can be an operator, method or any object of some class.
string = "poly"
num = 7
sequence = [1,2,3]
new_str = string * 3
new_num = 7 * 3
new_sequence = sequence * 3

print(new_str, new_num, new_sequence)

string = "poly"
sequence = [1,2,3]
print(len(string))
print(len(sequence))

#Inheritance
class Parent:
    #Members of the parent class
    pass

class Child(Parent):
    #Inherited members from parent class
    #Additional members of the child class
    pass

#Abstraction
#Abstraction can be seen both as a means for hiding important information 
# as well as unnecessary information in a block of code. 
# abc = abstract base class = a parent class
from abc import ABC
class ClassName(ABC):
    pass