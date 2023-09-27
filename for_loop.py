#for loop
#Example 1
"""
value= range(4)
# i = 0
for i in value:
    print(i)"""

#Example 2
"""
digits = [1,2,3,4]
for i in digits:
    print(i)
else:
    print("No digits left")"""

#Example 3
"""
person = {"name": "Alice", "age": 30, "city": "New York"}

for key, value in person.items():
    print(f"{key}: {value}")"""

#Example 4
"""
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num % 2 == 0:
        continue  # Skip even numbers
    print(num)"""

#Example 5
"""
fruits = ["apple", "banana", "cherry", "date"]

for fruit in fruits:
    if fruit == "cherry":
        break  # Exit the loop when "cherry" is encountered
    print(fruit)"""

#Example 6
"""
for i in range(3):
    for j in range(2):
        print(f"({i}, {j})")"""

#Example 7
"""
s="Python Programming"
for x in s:
    if x in 'aeiou':
      print(x)"""

#Example 8
"""
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=' ')
    print()"""

#Example 9
"""
numbers = [1, 2, 3, 4, 5]

for num in reversed(numbers):
    print(num)"""

#Example 10
"""
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")"""


#Example 11
"""
s="Hello World"
for x in s:
    if x in ' ':
        break
    print(x)"""

    


