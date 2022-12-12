print("Made by vlad")
import pyautogui, time
exit = input("Do you want start app:\n")
def start():
    choose = input("Ricroll or roblox:\n")
    if choose == "my":
        lopa = input("please enter file name example: file.txt:\n")
    if choose == "My":
        lopa = input("please enter file name example: file.txt:\n")
    if choose == "MY":
        lopa = input("please enter file name example: file.txt:\n")
    if choose == "ricroll":
        lopa = "haha.txt"
    if choose == "Ricroll":
        lopa = "haha.txt"
    if choose == "RICROLL":
        lopa = "haha.txt"
    if choose == "roblox":
        lopa = "rb.txt"
    if choose == "Roblox":
        lopa = "rb.txt"
    if choose == "ROBLOX":
        lopa = "rb.txt"

    print("wait 5 second")
    time.sleep(5)
    f = open(lopa, "r")
    for word in f:
        pyautogui.typewrite(word)
        pyautogui.press("enter")
        print("Message sending")
if exit == "yes":
    start()
if exit == "Yes":
    start()
if exit == "YES":
    start()
if exit == "no":
    print("Have a nice day")
    exit
if exit == "No":
    print("Have a nice day")
    exit
if exit == "NO":
    print("Have a nice day")
    exit
