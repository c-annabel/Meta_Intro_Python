a='a-string'
print(a)

b="b-string"
print(b)

c='I am a long string'
print(c)

d='I am a '\
    'long string '\
        'with a back slash'
print(d)

print(a+b)

print(len(a))

print(a[2])

def type_casting00():
    age = 55
    print(type(str(age)))

    print(float(age))

print('Hellow', 'you!', sep=', ')

#Direct formatting
x=1
y=2
z=x+y
print('Adding the value of {} and {} = {}'.format(x,y,z))
print('Adding {1} and {0} = {2}'.format(x,y,z)) #Output formating


# print("Where do you live?")
# location = input() 
# print("So you live in " + location)
print(input("I live in ? "))

num1 = input('Enter a number: ')
num2 = input('Second number: ')
print(type(num1))
print(num1, num2, num1+num2, int(num1)+int(num2))
print(num1+'+'+num2)
print('Hello {} & {}'.format(num1, num2))

