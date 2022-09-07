import random

#pick a file:
#f_name = input('Type the file name: ')
#file = open(f_name) # "r" omitted as it's the default

file = open('12_01_petnames.txt', 'r')
f_content = file.read()

f_content_list = f_content.split("\n")

try:
    #print(f_content)  #print all as a string
    #print(f_content_list) #print a splited string
    # for x in f_content:
    #     print(x)
    #import random module and use choice function
    print(random.choice(f_content_list))
except FileNotFoundError as e:
    print("ERROR", e)


file.close()