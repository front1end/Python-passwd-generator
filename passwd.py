import random

password_length = 38

characters = "any-symbol"

password = ""   

for index in range(password_length):
    password = password + random.choice(characters)

print("Password generated: {}".format(password))
