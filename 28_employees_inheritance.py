class Employees:
    def __init__(self,name,last) -> None:
        self.name = name
        self.last = last

class Supervisors(Employees):
    def __init__(self, name, last, password) -> None:
        super().__init__(name, last)
        self.password = password

class Chefs(Employees):
    def leave_request(self,days):
        return "May I take a leave for " + str(days) + " days?"

andrian = Supervisors("Andrian", "A", "apple")
emily = Chefs("Emily", "E")
juno = Chefs("Juno", "J")

print(emily.leave_request(3))
print(andrian.password)
print(emily.name)

#------Examples-----------------------#
#multiple inheritance#
class A:
   a = 1
   
class B:
   b = 2
   
class C(A, B):
   pass

c = C()
print(c.a, c.b)

#Multi-level inheritance#
class A:
   a = 1

class B(A):
   a = 2

class C(B):
   pass

c = C()
print(c.a)

# Built-in functions
# issubclass():
print(issubclass(A,B)) #False
print(issubclass(B,A)) #True ( Is B subclass of A? )

# isinstance():
print(isinstance(c,A))
print(isinstance(c,C))

#super() function
class Fruit():
    def __init__(self, fruit):
        print('Fruit type: ', fruit)

class FruitFlavour(Fruit):
    def __init__(self):
        super().__init__('Apple')
        print('Apple is sweet')

apple = FruitFlavour()