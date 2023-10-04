#Dictionary {} Key:Value

person={
    'name':'Nuzhat',
    'age':'24',
    'Salary':'200000'
}
#OR
person=dict({ 'name':'Nuzhat',
    'age':'24',
    'Salary':'200000'})

print(person['Salary'])
print(len(person))
print(type(person))

#in operator
print('age' in person)

#Keys
pkeys=person.keys()
print(pkeys)

#Values
pvalues=person.values()
print(pvalues)

#Key:Value
for key, value in person.items():
    print(f"{key}:{value}")

#items
print(person.items())  

#for
for x in person.items():
    print(x)

for (a,b) in person.items():
    print("a:",a,"b:",b)

#UPDATE
person['age']=20
person.update({'name':'Fatima'})
print(person)

#Add New
person['country']="Pakistan"
print(person)

#Copy
another_person=person.copy()
print(another_person)
