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


delay_print("Welcome to Rise of Tyrants.\n")
time.sleep(10)
delay_print("Downloading...\n")
print("__________")
print("|________|")
time.sleep(1)
print("__________")
print("||_______|")
time.sleep(1)
print("__________")
print("|||______|")
time.sleep(1)
print("__________")
print("||||_____|")
time.sleep(1)
print("__________")
print("|||||____|")
time.sleep(1)
print("__________")
print("||||||___|")
time.sleep(1)
print("__________")
print("|||||||__|")
time.sleep(1)
print("__________")
print("||||||||_|")
time.sleep(1)
print("__________")
print("||||||||||")
time.sleep(2)
delay_print("Done!\n")
time.sleep(10)

delay_print("The land of Tyranus is wreacked in flames... 5,000 years ago (3500 BC) 5 brothers, Rurik, Temujin (later named Ghengis Khan), Olav, Mergen, Woden had found a great resourceful land and they split the land between them making capitals of their land, Kiev for Rurik, Karakorum for Temujin, Trondheim for OLav, Constantonople for Mergen and Aachen for Woden. As they settled new cities and expanded their empires, by the time they were 50 - in 3470 BC - Tyranus, Woden's son, was plotting to start a war between the mighty empires, The Kingdom of the Nords, The Kingdon of the Mongols, Rus, The Ottoman Empire and The Holy Roman Empire, now ruled by Tyranus after Woden mysteriously died. The war was fought for many years and then, in 1495, The Ottoman Empire's mainland was tooken by The Holy Roman Empire but Constantonople was not... No one could get through the walls of Constsantonople.\n")

characterName = input("What is your character going to be called? ")
time.sleep(2.5)
response = f'Hi {characterName}\n'
delay_print(response)
time.sleep(2.5)
age = input("What will your character's age be? ")
time.sleep(2.5)
response = f'Ok you are {age} years old.'
delay_print(response)
kingdom = input("What kingdom do you want to be from? A. Rus B. The Empire of the Mongols C. The Empire of the Mongols D. The Kingdom of the Nords E. The Holy Roman Empire ")
time.sleep(2.5)
response = f'You will be from {kingdom}.'
characterType = input("What type of character do you want to be?. You could be a warrior, a bowman, a mage or cavalry. Warriors have 100 hp, 110 defence and 90 attack. Bowmans have 90 hp, 100 defence and 110 attack. Mages have 110 hp, 110 defence and 80 attack. Cavalry have 110 hp, 80 defence and 110 attack. All of these characters also have abilitys and weapons")
time.sleep(5)
response = f'Ok you will be called {characterName}, your age will be {age}, you will be a {characterType} and you will be from the {kingdom}'
delay_print(response)
