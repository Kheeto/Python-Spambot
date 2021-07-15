prequired = {'pyautogui', 'time'}
import pyautogui as bot
import time as t
import pip
from os import system, name
def clearConsole():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
def install(pname):
    pip.main(['install', pname])
def spam():
    spamfile = open("text.spambot", 'r')
    lines = 0
    for line in spamfile:
        lines+=1
        bot.typewrite(line)
        bot.press("enter")
        t.sleep(int(delay))
    clearConsole()
    print("""
   _____ _____        __  __   ____   ____ _______ 
  / ____|  __ \ /\   |  \/  | |  _ \ / __ \__   __|
 | (___ | |__) /  \  | \  / | | |_) | |  | | | |   
  \___ \|  ___/ /\ \ | |\/| | |  _ <| |  | | | |   
  ____) | |  / ____ \| |  | | | |_) | |__| | | |   
 |_____/|_| /_/    \_\_|  |_| |____/ \____/  |_|   
                                                   
By Kheeto#9999 on Discord
This is an open source Spam-Bot also avalaible on Git-Hub.
    """)
    print("-----------------------------------------")
    print("Successful spammed "+str(lines)+" lines.")
    input("Press enter to close the program.")
system("title DOWNLOADING NEEDED LIBRARIES")
for pname in prequired:
    install(pname)
clearConsole()
system("title SpamBot by Kheeto#9999 on Discord")
print("""
   _____ _____        __  __   ____   ____ _______ 
  / ____|  __ \ /\   |  \/  | |  _ \ / __ \__   __|
 | (___ | |__) /  \  | \  / | | |_) | |  | | | |   
  \___ \|  ___/ /\ \ | |\/| | |  _ <| |  | | | |   
  ____) | |  / ____ \| |  | | | |_) | |__| | | |   
 |_____/|_| /_/    \_\_|  |_| |____/ \____/  |_|   
                                                   
By Kheeto#9999 on Discord
""")
t.sleep(0.5)
print("I'll automatically write for you the text in \"text.spambot\" file!")
delay = input("Please provide a time delay between the lines of the file\n")
input("Click enter, then click on where you want to spam and wait 5 seconds ")
t.sleep(5)
spam()

