#GoldXP Exercise1
# import random
# def get_random_temp():
#     random_temp = random.randrange(-10, 40)
#     print(int(random_temp),"°C")
#
#
# def main():
#      temp=get_random_temp()
#      print("The temperature right now is ", temp)
#      if temp < 0:
#          print("Brrr, that’s freezing! Wear some extra layers today")
#      elif temp >= 0 and temp <=23:
#          print("Quite chilly! Don’t forget your coat")
#      elif temp >=24 and temp <= 32:
#          print("Such a nice weather!")
#      elif temp >=33 and temp <= 40:
#          print("Time to hit the beach!")
#      else:
#          print("...")
# main()
# #ex4/
# import random
# def get_random_temp(season=['Winter','Spring','Summer','Autumn']):
#     winter = random.randrange(-10, 16)
#     spring = random.randrange(17, 22)
#     summer = random.randrange(23, 32)
#     autumn = random.randrange(0, 21)
#     print(season, ' is ',int(winter),"°C")
#     print(season, ' is ', int(spring), "°C")
#     print(season, ' is ', int(summer), "°C")
#     print(season, ' is ', int(autumn), "°C")
# def main():
#      temp= get_random_temp()
#
#      print("The temperature right now is ", temp)
#      if temp < 0:
#          print("Brrr, that’s freezing! Wear some extra layers today")
#      elif temp >= 0 and temp <=23:
#          print("Quite chilly! Don’t forget your coat")
#      elif temp >=24 and temp <= 32:
#          print("Such a nice weather!")
#      elif temp >=33 and temp <= 40:
#          print("Time to hit the beach!")
#      else:
#          print("...")
# main()

#GoldXP2 Exercise1
import random
def throw_dice():
    random_dice_num = random.randrange(1, 6)

    def throw_until_doubles():
        dice1 = int(random_dice_num)
        dice2 = int(random_dice_num)
        print(dice1,dice2)
        while dice1 != dice2:
            print(dice1 , dice2)
    throw_until_doubles()
throw_dice()