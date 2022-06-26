import random

password_length = 38

characters = "/a@fBrpBATL!6^ggGa;F!\5YS2q@:>"

password = ""   

for index in range(password_length):
    password = password + random.choice(characters)

print("Password generated: {}".format(password))
