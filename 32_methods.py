# Example 1
class A:
   def a(self):
       return "Function inside A"

class B:
    def a(self):
        return "Function inside B-a"
    def b(self):
        return "Function inside B-b"

class C(B,A):
    def b(self):
        return "Function inside B-c"

# Driver code
c = C()
print(c.a())

# Example 2
class D(A, B):
    def b(self):
        return "Function inside D"

class E(B):
    def b(self):
        return "Function inside E"
        
# Example 4
class F(E, D):
    pass

f = F()
print(f.b())
print(F.mro())