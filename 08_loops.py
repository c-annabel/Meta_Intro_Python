# favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisu', 'Chocolate Cake']

# for i in range(10):
#     print('Looping..',i)

# for item in favorites:
#     print('I like this deserts', item)

# for idx,item in enumerate(favorites):
#     print(idx, item)

# count = 0

# while count < len(favorites):
#     print('W - I like this desert', favorites[count])
#     count += 1

#--------Nested Loop Process--------*

# list1 = [1,2,3,4,5,6,7,8,9]
# list2 = [1,2,3,4,5,6,7,8,9]

# count = 0
# #outer loop
# for x in list1:
#     count += 1
#     #inner loop
#     for y in list2:
#         count += 1

# print(count)

#---The larger the array, the longer it takes ----#
import time
start_time = time.time()

#outer loop
for i in range(20):
    #inner loop
    for j in range(20):
        print(j, end = " ") # use of 'end ='
    print( )

print(round((time.time() - start_time), 2))