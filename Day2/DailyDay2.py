from datetime import datetime,timedelta
#Taking input from user and converting it to datetime object”“”
birthday = input('What is your birthday? ex. DD/MM/YYYY')
birthday_convert_to_date = datetime.strptime(birthday, "%d/%m/%Y")
#"Specifing the current date”“”
current_date = datetime.now()
#"age”“”
age = int(current_date.year - birthday_convert_to_date.year)
age_to_string = str(age)
last_digit_age = int(age_to_string[-1])
candles = 'i' * last_digit_age
cake = f'''\n       ___{candles}___
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:b:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~'''
print(cake)
cake2 = f'''       ___{candles}___   \n      |:H:a:p:p:y:|   \n    __|___________|__   \n    |^^^^^^^^^^^^^^^^^|   \n    |:b:i:r:t:h:d:a:y:|   \n    |                 |    \n    ~~~~~~~~~~~~~~~~~~~'''
if birthday_convert_to_date.year % 4 == 0:
    print(cake *2)
