from pyfiglet import Figlet;
from time import sleep;
from colorama import init;
from termcolor import colored;
from folder.menu import Menu;

init();

def RestaurantGreeting():
   f = Figlet();
   print(colored(f.renderText("WELCOME TO..."), "light_yellow", attrs=["bold"]))
   sleep(1.75)
   print(colored(f.renderText("YUMMY TUMMY RESTAURANT!!!"), "magenta", attrs=["bold"]));
   sleep(1.75)
   return;

def GreetingInterface():
   RestaurantGreeting();
   print(f"\n{'*'*15}\n");
   print("OUR CURRENT MENU!!!");
   print(Menu)   

