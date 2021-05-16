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
characterType = input("What type of character do you want to be?. You could be a warrior, a bowman, a mage or cavalry. Warriors have 100 hp, 110 defence and 90 attack. Bowmen have 90 hp, 100 defence and 110 attack. Mages have 110 hp, 110 defence and 80 attack. Cavalry have 110 hp, 80 defence and 110 attack. All of these characters also have abilitys and weapons")
time.sleep(5)
response = f'Ok you will be called {characterName}, your age will be {age}, you will be a {characterType} and you will be from the {kingdom}'
delay_print(response)
time.sleep(10)
response = f'Wake up... Wake up... *whispers*... WAKE UP {characterName}!!!\n'
delay_print(response)
firstReatcion = input("Response Choices:A. Wake up and punch.B. Scream.C. Say I dont want to and fall back sleep.D. You have to type A B C or D!\n")
if firstReatcion == 'A':
    delay_print("Ouch! Must of been a big bang on the head! We are not going to kill you.\n")
elif firstReatcion == 'B':
    delay_print("Wow there! It's Ok, we're not going to kill you, but they are so quikly come with us!\n")
elif firstReatcion == 'C':
    delay_print("Come on you idiot! You'll get everyone killed including you!\n")
secondReaction = input("Response Choices:B. How can I trust you?C. Get away from me!\n")
#if secondReaction == 'A' and kingdom == 'Rus':
    #delay_print("I am Grand Prince Alexander. I am Prince Adrik. And I am Boyar Ivan")
#elif secondReaction == 'A' and kingdom == 'Nords':
    #delay_print("I am Jarl Anderson. I am King Erik. And I am Jarl Frode, we are from the Nord Empire.\n")
#elif secondReaction == 'A' and kingdom == 'Ottoman':
    #delay_print("I am Sultan Suleiman. I am Emir Utkan. And I am Shemsi Pasha, we are from the Ottoman Empire.\n")
#elif secondReaction == 'A' and kingdom == 'Urania':
    #delay_print("I am Emperor Frederick 'Red Beard' Barbarossa. I am Legio IX Hispana. and I am Michael Adolph von Althann, we are from the Holy Roman Empire.\n")
#elif secondReaction == 'A' and kingdom == 'Mongols':
    #delay_print("I am Genghis Khan. I am Batu Khan. and I am Jochi Khan, we are from the Mongolian Empire\n")
if secondReaction == 'A' and kingdom == 'Rus':
    delay_print("We are the leaders of Rus! I am the Tsar and these are the top Boyars.\n")
elif secondReaction == 'A' and kingdom == 'Nords':
    delay_print("We are the leaders of the vikings! I am the king and these are the top Jarls.\n")
elif secondReaction == 'A' and kingdom == 'Ottoman':
    delay_print("We are the leaders of the Ottoman Empire! I am the Sultan and these are the top Emirs.\n")
elif secondReaction == 'A' and kingdom == 'Urania':
    delay_print("We are the leaders of the Holy Roman Empire! I am the Emperor and these are my top men\n")
elif secondReaction == 'A' and kingdom == 'Mongols':
    delay_print("We are the leaders of the Mongolian Empire! I am the Khan and these are my sons.\n")
elif secondReaction == 'B':
    delay_print("We told you, we are not going to kill you!\n")
delay_print("You were just wondering about like a normal person but then a band of raiders came and fought you, you fought back but there was too many of them. We found you unconcious and temporarily blind. The bandits got away. We are still at the battle site so I suggest we should get out of here before more bandits come.\n")
