my_list = [1,2,3]
new_list = [1,2,3]

# not pure function
# data has been manipulated at the global scope 
# from inside the scope of the function

def add_to_list(item):
    return my_list.append(item)
add_to_list(4)
print(my_list)

# pure function, doesn't manipulate the original list
my_list = new_list
def add_to_list(lst, item):
    nl = lst.copy()
    nl.append(item)
    return nl

new_list = add_to_list(my_list, 4)
print(my_list)
print(new_list)