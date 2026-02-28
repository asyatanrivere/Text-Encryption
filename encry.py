import random
import string
chars= " " + string.punctuation + string.ascii_letters + string.digits
# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
chars=list(chars)
key=chars.copy()

random.shuffle(key)

sentence = input("Enter the sentence: ")
new_sentence=""
for letter in sentence:
    index=chars.index(letter)
    letter=key[index]
    new_sentence+=key[index]
print(f"Original message: {sentence}")
print(f"Encrypted message: {new_sentence}")

    



