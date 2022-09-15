#Comprehensions in Python are a way to create a new sequence 
# from an already existing sequence.

#List comprehension
data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

#Regular for loop
for x in range(len(data)):
    data[x] = data[x] + 2

#EX1: updating the same list
data = [x+2 for x in data]
print("Creating new list: ", data)

#EX2: creating a different list with updated values
new_data = [x*3 for x in data]
print("Creating new list: ", new_data)

#EX3: with an if-condition:multiples of 2:
twox = [x for x in new_data if x%2 == 0]
print("Divisible by two: ", twox)

#EX4: update the list with the if condition
twoxplus = [x+1 for x in new_data if x%2 == 0]
print("Divisible by 2 plus one: ", twoxplus)

#EX5: using range function:
eights = [x for x in range(100) if x%8 == 0]
print("Eights: ", eights)

def hyphendiv():
    for y in range(60):
         print('-', end='')
    print('\n')

hyphendiv()

#Dictionary comprehension
# dict = {key:value  for key, value in <sequence> if <condition>}

# using range() function and no input list
usingrange = {x:x+2 for x in range(10)}
print("Using range(): ", usingrange)

# Lists
weekdays = ["lundi", 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche']
numbers= [1,2,3,4,5,6,7,8]

# using one input list
numdict = {x:x**2 for x in numbers}
print("Using one input list to create dict: ", numdict)

# using two input lists (shorter list is used)
week_dict={key:value for (key, value) in zip(numbers, weekdays)}
print("Using two lists: ", week_dict)

hyphendiv()

#Set comprehension (curly brackets)
set_a = {x for x in range(10,20) if x not in [12,14,16]}
print("Set: ", set_a)

hyphendiv()

# Generator comprehension
# with the variation of using curved brackets instead of square brackets. 
# They are also more memory efficient as compared to list comprehensions.

data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
gen_obj = (x for x in data)
print(gen_obj) #can't be directly accessed
print(type(gen_obj))
for items in gen_obj:
    print(items, end=' ')

print('\n')
hyphendiv()

def square(num):
    return num + 3

newdata = map(square, data)
newdata2 = [x+3 for x in data]
print(newdata)
print(newdata2)
for x in newdata:
    print(x, end=' ')