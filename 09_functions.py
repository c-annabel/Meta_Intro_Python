bill = 175.00

tax_rate = 15

total_tax = (bill * tax_rate) / 100.00

print('Total Tax 1:', total_tax)

# dynamic function
def calculate_tax(bill, tax_rate):
    return round((bill * tax_rate) / 100.00, 2)

print('Total Tax 2:', calculate_tax(164.33, 22))

# Global Scope

special = 5

def get_total(a, b):
    #enclosed scope variable declared inside a function
    total = a + b
    print(special)

    def double_it():
        #local variable
        double = total * 2
        print(special)

    double_it()

    return total

# Built-in scope

# Built-in scope refers to the reserved keywords that Python uses 
# for its built-in functions, such as print, def, for, in, and so forth.  
# Functions with built-in scope can be accessed at any level.