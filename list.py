#List [Store multiple items in single variable.]
#Example1
"""fruit_list=["apple","mango","orange","banana","grapes","pomegranate" ]
print(type(fruit_list))
print(len(fruit_list))
print(fruit_list[3])
print(fruit_list[0:2])
print("mango" in fruit_list)"""

# #To update or chnage items
#Example 2
"""fruit_list[0]="Peach"
fruit_list.insert(2, "pineapple")
fruit_list.append("onion")
fruit_list.remove("onion")
fruit_list.sort()
print(fruit_list)
"""

#for loop
#Example 3
"""for index, fruit in enumerate(fruit_list):
    print(f"Index {index}: {fruit}")"""

#Example 4
"""data=[("Ali",20),("Umer",21),("Usman",25)]
for names, age in data:
    print(f"name:{names}, age:{age}")"""

#Example 5

"""numbers=[1,2,4,6,7,9]
for num in reversed(numbers):
    print(num)"""

#Example 6
"""marks=[20,25,40,30.5,10]
max=marks[0]
for m in marks:
    if m > max:
        max=m
print(max)"""

#While loop

#Example 7

"""l=len(marks)
i=0
while i < l:
    print(marks[i])
    i=i+1"""

#List comprehensions

#Example 8
"""numbers=[20,50,15,27,22,90,56,13]
even=[m for m in numbers if m%2==0]
print(even)
#OR

even=[]
for n in numbers:
    if n%2==0:
        even.append(n)
print(even)   """     
