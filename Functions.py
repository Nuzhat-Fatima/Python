#A function is a block of code that performs a specific task.
#There are two types of function in Python programming:
#1:Standard library functions - These are built-in functions in Python that are available to use.
#2:User-defined functions - We can create our own functions based on our requirements.

def display():
    print("Hello")
display()    

#Adding 2 variables
def total(a,b):
    s= a + b
    print("Sum=",s)
total(10,2)  

#Default Parameter value
def total(a=20, b=30):
    sum= a + b
    print(sum)
total()           #uses default value of a and b
total(a=1)        #value of a=1 and b=30(default)
total(a=1, b=59)  #uses given values instead of default

#Keyword arguments
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

# Using keyword arguments to call the function
greet(name="Alice", age=30)

def numbers(a,b,c):
    add= a+b+c
    print(add)

numbers(a=1, b=2, c=3)    

def add(a, b):
    result = a + b
    return result

sum = add(3, 5)  # The return value (8) is assigned to the variable 'sum'
print(sum)

#To check even number
def is_even(n):
    if n%2==0:
        return True
    else:
        return False
flag=is_even(12)
if flag:
    print("even")
else:
    print("odd")        


#To check prime number
def check_number(n):
    i=2
    is_prime= True
    while i<n:
        if n%i==0:
            is_prime=False
            break
        i=i+1
    return is_prime
#n=int(input("enter number:"))
flag=check_number(7)
if flag:
    print("prime")
else:
    print("not prime")      

#Arbitrary arguments(if we don't know how many arguments we need to pass, we can add * before parameter)
def show(*args):
    print(args)
show(10,20,30,40)  

def show_(a,b,*args):
    print(a,b,args)
show_(10,20,1,2,3,4,5,6) 


      
