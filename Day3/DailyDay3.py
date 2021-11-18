# method 1
# def encrypt(text, s):
#     result = ""
#
#     # traverse text
#     for i in range(len(text)):
#         char = text[i]
#
#         # Encrypt uppercase characters
#         if (char.isupper()):
#             result += chr((ord(char) + s - 65) % 26 + 65)
#
#             # Encrypt lowercase characters
#         else:
#             result += chr((ord(char) + s - 97) % 26 + 97)
#
#     return result
#
#
# # def decrypt(ciphertext, s):
#
#
# text = input("Enter a message to be ciphered")
# s = 4
# Cipher = encrypt(text, s)
#
# print("Text : " + text)
# print("Shift : " + str(s))
# print("Cipher: " + encrypt(text, s))

#method2
import string
alphabet_lower = list(string.ascii_lowercase)
alphabet_upper = list(string.ascii_uppercase)

def userCypher(message, shift, encrypt_or_decrypt):
    cyphered_message=''
    extra_chars=['',',','.','!',"'",'?']
    for letter in message:
        if letter in extra_chars:
            cyphered_message += letter
        else:
            upper_or_lower = alphabet_upper
            if letter.isupper():
