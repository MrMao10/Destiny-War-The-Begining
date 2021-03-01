import time
import sys
from characterclasses import *

#delay printing

def delay_print(s):
    for c in s :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

delay_print("Warning! Will be addictive!")
time.sleep(5)


delay_print("Welcome to Mount and Blade 1. I will tell you how to play. You will have to make choices which include fighting or speaking with people. Depending on your level, you will do more damage and will have more health ")
time.sleep(10)
delay_print("Downloading...")
time.sleep(10)
delay_print("Done!")

characterName = input("What is your character going to be called?")
time.sleep(5)
response = f'Hi {characterName}'
delay_print(response)
time.sleep(5)
age = input("What will your character's age be?")
time.sleep(5)
if age.isdigit False:
    age1 = input("Invalid age. Enter new age!")
    response = f'Ok you are {age1} years old'
    delay_print(response)
else:
    response = f'Ok you are {age} years old'
    delay_print(response)
faction = input("What faction will you be from? The Vaegirs, Swadians, Nords, Sarranid Sultanates, Khergit Khanates.")
time.sleep(5)
response = f'Ok you will be from {faction}'
characterType = input("What type of character do you want to be?. You could be a warrior, a bowman, a mage or cavalry. Warriors have 100 hp, 110 defence and 90 attack. Bowmans have 90 hp, 100 defence and 110 attack. Mages have 110 hp, 110 defence and 80 attack. Cavalry have 110 hp, 80 defence and 110 attack. All of these characters also have abilitys and weapons")
time.sleep(10)
response = f'Ok you will be called {characterName}, your age will be {age}, you will be a {characterType} and you will be from the {faction}'
delay_print(response)
    
