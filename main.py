if __name__ == "__main__":
   from folder.menu import Menu;
   from folder.functions.restaurant_greeting import GreetingInterface;
   from folder.functions.app import App;
   from termcolor import colored;
   from colorama import init;
   
   init();

   GreetingInterface();
   input("Press any key to continue with your order...")
   ItemNumber, Quantity = 0, 0;
   _orderID = 1;
   finished = False;

   try:
      Budget:float = float(57.00);

      while (finished == False) and (Budget > 1.99):
         print("Your current Budget is now:", colored(Budget, "light_green", attrs=["bold"]));
         ItemNumber, Quantity = input("Enter the food item number (on the left) and the quantity you want to order => ").split();
         ItemNumber = int(ItemNumber);
         Quantity = int(Quantity);
         print(f"\n{'='*51}\n")
         OrderResult = App(ItemNumber, Quantity, Budget, _orderID);
         if isinstance(OrderResult, dict): 
            Budget = OrderResult.get("Budget");
            _orderID+=1;
         print(OrderResult, end=f"\n\n{'*'*51}\n\n");
         isDone = input("Are you finished???");
         print();
         finished = False if isDone in ["no", "n"] else True;
   except ValueError as err:
      print(f"Sorry... you MUST enter integers for itemNumber (you have {colored(ItemNumber, color='red', attrs=['bold'])}) and quantity (you have {colored(Quantity, color='red', attrs=['bold'])})!!! => {err}");
   except IndexError as err:
      print(f"It appears you selected an item number that is NOT on the menu. We only have 12 items and you selected {colored(ItemNumber, color='red', attrs=['bold'])} as an ItemNumber: {err}.");

   