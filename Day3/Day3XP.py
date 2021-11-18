# #exercise XP 1
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
#
# dictionary = dict(zip(keys,values))
# print(dictionary)


# #exercise XP 2
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
#
# age=int(input("Enter age or enter '0' to quit:"))
# price = []
# active= True
# while age != 0:
#     age=int(input("Enter age or enter '0' to quit:"))
#     # for i in list:
#     if age <= 3:
#           price.append(0)
#     elif age>3 and age<12:
#           price.append(10)
#     elif age== 0:
#           active = False
#     else:
#           price.append(15)
#print(sum(price))
# print(price)
# family_prices=zip(family.keys(),price)
# prices={}
# for i,j in family_prices:
#     prices[i]= j
# print(prices)

# #exercise XP 3
# brand={"name":["Zara"], "creation_date":["1975"], "creator_date":["Amancio Ortega Gaona"],"type_of_clothes":["men", "women" , "children" , "home"],
#        "international_competitors":["Gap","H&M","Benetton"], "number_stores":["7000"], "major_color": {"France":"blue","Spain":"red","US":["pink","green"]}}
#
# brand["number_stores"]=2
#
# print("Zara's clients are:", brand['type_of_clothes'][0:3] )
#
# brand["country_creation"]=["Spain"]
# if 'international_competitors' in brand:
#     brand['international_competitors'].append("Desigual")
#
# del brand['creation_date']
#
# print(brand)
# print(brand['international_competitors'][-1])
# print(brand['major_color']['US'])
# print(len(brand))
#
# print(brand.keys())
#
# more_on_zara = {"creation_date":["1975"], "number_stores":["10 000"]}
#
# brand.update(more_on_zara)
#
# print(brand.values())

#Exercise XP4
users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]

#1/

disney_users_A = {key: i for i, key in enumerate(users)}
print(disney_users_A)

#2/
disney_users_B = {}
for (index, val) in enumerate(users):
    disney_users_B[index] = val
print(disney_users_B)

#3/
users.sort()
print(users)
disney_users_C = {key: i for i, key in enumerate(users)}
print(disney_users_C)

#4/
users = ["Mickey", "Minnie", "Donald","Ariel","Pluto"]
result_dict = {}
for k, v in zip(users, list(range(len(users)))):
    if 'i' in k and k[0] in ['M','P']:
        result_dict[k] = v
for k, v in zip(list(range(len(users))), users):
    result_dict[k] = v
for k, v in zip(sorted(users), list(range(len(users)))):
    result_dict[k] = v

