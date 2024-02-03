import colorama
from colorama import Fore , Back , Style
colorama.init(autoreset=True)

print(Fore.BLUE+Back.YELLOW + "Hi My name is Ricky Yang " + Fore.YELLOW + Back.BLUE + "I am your Machine Learning Instructor")
print(Back.CYAN + "Hi My name is Ricky Yang")
print(Fore.RED + Back.GREEN + "Hi My name is Ricky Yang")