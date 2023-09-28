#Example 1
"""
count = 1
while count <=5:
    print(count)
    count= count+1
    """

#Example 2
"""
total = 0
num = 1
while num <= 10:
    total += num
    num += 1
print(f"The sum of numbers from 1 to 10 is {total}.")
"""
#Example 3
"""
while True:
    user_input=input("Enter 'yes' or 'no': ").lower()
    if user_input=='yes':
        print("you entered yes")
        break
    elif user_input=='no':
        print("you entered no")
        break
    else:
        print("Invalid Input")
"""

#Example 4
"""
password= "code"
attempts= 3
while attempts > 0:
    user_password=input("Enter Password: ")
    if user_password==password:
        print("Access Granted")
        break
    else:
        attempts -= 1
        print(f"Access denied,{attempts} attempts left. ")
else:
    print("Account locked") 
"""

#Example 5
"""
s="Python programming"
x=0
l=len(s)
while x < l:
    print(s[x])
    x= x + 1 
print("end") 
"""

#Example 6
"""
x = 1
while x <= 100:
    if x % 2 == 0:
        print(x)
    x += 1 
"""
# Example 7
"""
sum = 0
x = ' '
while x != 'N':
    x= input("enter number or N to exit: ")
    if x != 'N':
        sum += int(x)
print(sum)
"""

#NESTED WHILE LOOP
"""
i = 1           #Prints 5 rows and 5 colums
while i <= 5:
    j = 1
    while j <= 5:
        print(j,end=' ')
        j=j+1
    print()
    i=i+1
"""    
#Prints numbers in right angle triangle shape
"""
i=1
while i<=5:
    j=1
    while j<=i:
        print(j,end=' ')
        j+=1
    print()
    i+=1
"""
