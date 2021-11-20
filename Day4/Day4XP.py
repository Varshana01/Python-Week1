# #XP1 exercise 1
# def display_message():
#     print("I am learning Python!")
# display_message()
#
# #XP1 exercise 2
# def favorite_book(title):
#     print("One of my favorite books is " + title)
# favorite_book(title='Harry Potter')

# #XP1 exercise 3
# country = "Mauritius"
# def describe_city(city, country):
#     print(city, " is in ",country)
#
# describe_city('Cape Town','South Africa')

# #XP1 exercise 4
# import random
# def guess():
#    num=int(input("Enter a number from 1 to 100"))
#    print(num)
#    range=random.randrange(1,100)
#    print(int(range))
#
#    if num != range:
#        print("You lost")
#    else:
#        print("You win!")
# guess()

#XP1 exercise 5
##1,2,3/
# def make_shirt(size, text):
#     print("Shirt of size "+size + " with message: " + text)
# make_shirt(size='Medium', text='Hello')

# #4/
# def make_shirt(size='Large', text='I love Python'):
#     print("Shirt of size: "+ size + " with message:" + text)
# make_shirt()

# # 5/
# def make_shirt(size, text='I love Python'):
#     print("Shirt of size: "+ size + " and with message: " + text)
#
# make_shirt("Medium")
# make_shirt("Large")
# make_shirt("Small","Vitamin Sea")

# #6/
# def make_shirt(**kwargs):
#     print(kwargs)
# make_shirt(size='Small', text="Get 'em!")

# #XP1 exercise 6
#
# magician_names=["Apolla","Houdini","Blaine","Copperfield"]
# # def show_magicians():
# #     for i in magician_names:
# #         print("One of the magician is: "+i)
# # show_magicians()
#
# def show_magicians():
#     for i in magician_names:
#         print("One of the magician is: "+i)
#     def make_great():
#         for i in magician_names:
#             print("One of the magician is: "+ f"the Great {i}")
#     make_great()
# show_magicians()
