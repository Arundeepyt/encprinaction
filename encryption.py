import random
import string


chars=  " "+string.ascii_letters+string.digits+string.punctuation
chars=list(chars)
key=chars.copy()

random.shuffle(key)

print(f"chars : {chars}")
print(f"key : {key}")

#ENCPYT
plain_text = input("Enter the text to be encrypted: ")
cipher_text = ""

for letter in plain_text:
    index=chars.index(letter)
    cipher_text +=key[index]

    print(f"original text : {plain_text}")
    print(f"encrypted text : {cipher_text}")