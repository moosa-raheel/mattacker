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
print(colored(heading,"cyan"))
print(colored("\n\n1) ","yellow"),colored("Facebook\n\n","green"))

print(colored("Enter your choice : ","red"),end=" ")

choice = int(input())
if(choice==1):
    if platform == "win32":
        os.system("python sites/manage.py runserver")
    else:
        os.system("python3 sites/manage.py runserver")