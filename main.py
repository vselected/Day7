# Lambda Expressions Map and Filter FUnctions
print("Map Function")

def square(number):
    return number**2

my_numbers = [1,2,3,4,5]

#Ex1
for item in map(square,my_numbers):
    print(item)

#Ex2
print(list(map(square,my_numbers)))

def splicer(mystring):
    if len(mystring)%2 == 0:
        return "Even"
    else:
        return mystring[0]

names = ["Andy", "Eve", "Sally"]

print(list(map(splicer,names)))

# Filter Function
print("\nFILTER FUNCTION")

def check_even(number):
    return number%2 == 0

numbers = [1,2,3,4,5,6]

for n in filter(check_even,numbers):
    print(n)

print(list(filter(check_even,numbers)))

# Lambda Expression
print("\nLAMBDA EXPRESSION")

square = lambda num: num ** 2
print(square(6))

print(list(map(lambda  num:num**2,my_numbers)))

#Nested Statements and Scope

#GLOBAL
name = "THIS IS A GLOBAL STRING"

def greet():
    # ENCLOSING
    #name = "Sammy"

    def hello():
        #name = "IM A LOCAL"
        print("Hello "+name)

    hello()

greet()


x = 50

def func():
    global x
    print(f"X is {x}")

    #LOCAL REASSIGNMENT ON A GLOBAL VARIABLE!
    x = "New Value"
    print(f"I just locally changed global X to {x}")

func()


