#ADD STRINGS, CONCATENATION

"""
s1="Great"
s2="Pakistan"
s3=s1+' '+s2
# print(s3)
print((s3+' ')*2)
print((s3+'\n')*2)
"""

#String Format[(.format (used for string formatting)]

item="Apple"
qty=3
price=40
x="I want {}kg of {} of price {}."

print(x.format(qty,item,price))

#Print in lower and upper case

print(x.lower())
print(x.upper())

#Escaping

t="Pakistan \nis a great country."
t1="Pakistan \tis a great country."
t2="Pakistan is a \"great\" country."
print(t)
print(t1)
print(t2)
