sentence = input("Enter a string of 10 characters long")
if len(sentence) < 10:
    print("String not long enough")
elif len(sentence) > 10:
    print("string too long")
else:
    print(f"{sentence[0]}\n {sentence[-1]}")

result = " "
for c in sentence:
    result += c
    print(result)

import random
str_list = list(sentence)
random.shuffle(str_list)
str_final=''.join(str_list)
print(str_final)






