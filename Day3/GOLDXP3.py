# #GOLD XP Exercise 1
# birthdays ={'Yas':'2001/05/30','Varsh':'2201/09/01','Hem':'2001/08/18','Teesha':'2007/08/24','Ahanaa':'2020/02/28'}
# print('Welcome! You can look up the birthdays of the people in the list!')
# name = input("Enter a name")
# if name in birthdays:
#     print(name,"has birthday on", birthdays[name])
#
# #GOLD XP Exercise 2
# print(birthdays)
# if name not in birthdays:
#     print(f"Sorry, we don’t have the birthday information for {name} ")
#
# #GOLD XO Exercise 3
#
# user_name = input("Enter your name")
#
# user_birthdate=input("Enter your birthday (YYYY/MM/DD)")
#     if user_name in birthdays:
#         print(birthdays)
#
# user_birthday={user_name:user_birthdate}
# birthdays[user_name]=user_birthdate
# print(birthdays)

# #GOLD XO Exercise 4
# items={
#     "banana": 4,
#     "apple": 2,
#     "orange": 1.5,
#     "pear": 3
# }
# for i in items:
#     print("A", i, "is",items[i] )
#     item={i:items[i]}
#     print(item)
# print("Total cost will be:",items['banana']+items['apple']+items['orange']+items['pear'])

#GOLD XO Exercise 5
car="Volkswagen, Toyota, Ford Motor, Honda, Chevrolet".split(",")
print(car)
print("The number of manufacturers are:", len(car))
car.reverse()
print(car)

counter_1=0
counter_2=0
for i in car:
    if "o" in i:
        counter_1+=1
    if "i" not in i:
        counter_2+=1
print(counter_1)
print(counter_2)

car_2=set(["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"])
print(car_2)