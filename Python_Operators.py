
#Arithemetic Operations
x=100
y=30
#Addition
z=x+y
#Subtraction
a=x-y
#Multiplication
b=x*y
#Division
c=x/y
#Modulus
d=x%y
#Exponentiation
e=x**y
#Floor Division
f=x//y
"""
print(z,a,b,c,d,e,f)
"""
#Comparison Operators
"""
x1=100
y1=300
#EQUAL
print(x1==y1)
#NOT EQUAL
print(x1 != y1)
#GREATER
print(x1 > y1)
#Less
print(x1 < y1)
#> than or == to
print(x1 >= y1)
#< than or == to
print(x1 <= y1)"""

#LOGICAL OPERATORS
#Logical AND
"""
x = True
y = False

result = x and y  # x is True and y is False, so the result is False
print(result) """   # Output: False

#Logical OR:if x is false then y, else x

"""
a = True
b = False

result = a or b  # a is True, so the result is True
print(result)"""   # Output: True

#Logical NOT
"""
c = True

result = not c  # c is True, so the result is the opposite, which is False
print(result)"""   # Output: False

#ASSIGNMENT OPERATORS
#Addition Assignment (+=)
"""
y = 10
y += 3  # Add 3 to y and assign the result to y (y is now 13)
print(y)
"""

#Subtraction Assignment (-=)
"""
z = 15
z -= 5  # Subtract 5 from z and assign the result to z (z is now 10)
print(z)
"""
#Multiplication Assignment (*=)
"""
a = 6
a *= 2  # Multiply a by 2 and assign the result to a (a is now 12)
print(a)
"""

#Division Assignment (/=)
"""
b = 8
b /= 4  # Divide b by 4 and assign the result to b (b is now 2.0)
print(b)
"""
#Modulus Assignment (%=)
"""
c = 11
c %= 3  # Calculate the remainder of c divided by 3 and assign the result to c (c is now 2)
print(c)"""

#Exponentiation Assignment (**=)
"""
d = 4
d **= 2  # Raise d to the power of 2 and assign the result to d (d is now 16)
print(d)"""

#Floor Division Assignment (//=)
"""
e = 9
e //= 2  # Perform floor division of e by 2 and assign the result to e (e is now 4)
print(e)
"""
#IDENTITY OPERATORS
#IS
"""
a = [1, 2, 3]
b = a  # b now refers to the same object as a

result = a is b  # a and b are the same object, so the result is True
print(result)"""    # Output: True

#IS NOT
"""
x = "hello"
y = "world"

result = x is not y  # x and y are different objects, so the result is True
print(result) """       # Output: True

#MEMBERSHIP OPERATORS
#IN
"""
fruits = ["apple", "banana", "cherry"]

result = "banana" in fruits  # Check if "banana" is in the list
print(result) """              # Output: True

#NOT IN
"""
colors = ("red", "green", "blue")

result = "yellow" not in colors  # Check if "yellow" is not in the tuple
print(result) """                  # Output: True

#BITWISE OPERATORS
#Bitwise AND (&):The & operator performs a bitwise AND operation between the corresponding bits of two integers. It returns 1 for each position where both bits are 1, and 0 otherwise
"""
a = 5  # Binary: 0101
b = 3  # Binary: 0011

result = a & b  # Bitwise AND: 0101 & 0011 = 0001
print(result)"""   # Output: 1

#Bitwise OR (|):The | operator performs a bitwise OR operation between the corresponding bits of two integers. It returns 1 for each position where at least one bit is 1.
"""
x = 12  # Binary: 1100
y = 5   # Binary: 0101

result = x | y  # Bitwise OR: 1100 | 0101 = 1101
print(result)"""   # Output: 13

#Bitwise NOT (~):The ~ operator is a unary operator that performs a bitwise NOT operation on each bit of an integer, inverting each bit.
"""
r = 7   # Binary: 0111

result = ~r  # Bitwise NOT: ~0111 = 1000 (in two's complement)
print(result) """ # Output: -8 (in decimal)

#Bitwise XOR (^):The ^ operator performs a bitwise XOR (exclusive OR) operation between the corresponding bits of two integers. It returns 1 for each position where the bits differ (one is 1 and the other is 0).
"""
p = 9   # Binary: 1001
q = 3   # Binary: 0011

result = p ^ q  # Bitwise XOR: 1001 ^ 0011 = 1010
print(result)"""   # Output: 10
