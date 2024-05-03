import os
import time
list_packages = []
try:
    from termcolor import colored
except ModuleNotFoundError:
    os.system("pip install termcolor")
    
print(colored("\nstart script.....\n","blue"))
time.sleep(1)
print(colored("Author : Moosa Raheel","light_green"))
time.sleep(1)
print(colored("\nchecking packages.....","green"))
time.sleep(2)
print(colored("\nhttps://github.com/moosa-raheel","light_blue"))

from rich.console import Console

# Create a console instance
console = Console()

# Display text in bold
console.print("[bold]This is bold text[/bold]")

