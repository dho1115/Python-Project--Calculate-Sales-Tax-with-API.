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

MenuTitle = colored(f"\n{' '*35}OUR CURRENT MENU ITEMS!!!\n", on_color='on_light_yellow', attrs=["bold"]);

def colorMenu():
   coloredMenu = [];

   for i in Menu:
      if i[0]%2==0:
         i = colored(i, "light_magenta", attrs=["bold"])
         print(i)
      else:
         i = colored(i, "light_yellow", attrs=["bold"])
         print(i)
   
   coloredMenu = [*coloredMenu, i]

   return coloredMenu;


def GreetingInterface(): 
   RestaurantGreeting();
   print();
   print(MenuTitle)
   print(colorMenu())

