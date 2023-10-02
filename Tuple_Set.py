#TUPLE()****************
#Not changeable
#Used to store multiple items in a single variable

week_days=("Mon","Tue","Wed","Thu","Fri","Sat","Sun")
#UNPACKING
(day1,day2,day3,day4,day5,day6,day7)=week_days
print(day1)
print(day2)
print(day3)
print(day4)
print(day5)
print(day6)
print(day7)

person=("Ali", 20 , "USA")
name,age,country=person
print(f"{name} is {age} yeasr old and lives in {country}.")
print(f"Name: {name}, age: {age}, country:{country}")
#Count how many times Mon is present in Tuple
print(week_days.count("Mon"))

#Tells index of specific value
print(week_days.index("Thu"))

#CONSTRUCTOR
months=tuple(("Jan","Feb","Mar"))

#if
if "April" in months:
    print(" 'Jan is in months' ")
else:
    print("This month is not present")  

#SETS {}***********************
#It is UNORDER and UNINDEX, Duplicate is not allowed

country_names={"USA","UAE","Africa","Arab","Canada"}
print(country_names)

print(type(country_names))
print(len(country_names))

#To add values in set
country_names.add("Pakistan")

#To remove specific value
country_names.remove("Arab")

print(country_names)

#CONSTRUCTOR
country_names=set(("Pak","Ind","USA"))

