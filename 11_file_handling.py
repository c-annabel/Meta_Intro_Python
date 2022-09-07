# file = open('11_HelloPython.txt', mode='r')

# data = file.readline()

# print(data)

# file.close()

# Second Example
# with open('11_01_hello_python.txt', mode='r') as file:

#     data = file.readline()
# readlines() reads the entire contents of the file
# and return it in an ordered list.

#     print(len(data)) --> print number of lines
#     print(file.read(5)) -->print only the first 5 characters
#     print(data)

#Creating Files
# with open('11_02_newfile.txt', 'w') as file:
#     #overwrite each time
#     file.write("This is a new file created!")
#     file.writelines([" This is second.", " This is thrid.", "\nThis is a new line."])

try:
  #with open('11_02_newfile.txt', 'a') as file:
   with open('sample/newfile.txt', 'a') as file:
    file.write("\nAppending texts.")
except FileNotFoundError as e:
    print("ERROR", e)


