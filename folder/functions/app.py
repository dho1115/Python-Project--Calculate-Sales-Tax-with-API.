from folder.functions.OrderCost import SubTotal;
from folder.menu import Menu;
from folder.currentorders import CurrentOrders, CartTotal;
from termcolor import colored;
from colorama import init;

init();

def App(ItemNumber:int, Quantity:int, Budget:float, _orderID:int):
      global CurrentOrders
      global CartTotal

      try:
            Order:dict = SubTotal(Quantity, ItemNumber, Menu);

            if Order.get('total') > Budget: 
               raise ValueError(colored(f"Sorry, but the total of this order, ${Order.get('total')} CANNOT exceed your remaining budget of ${Budget}.", "red", attrs=['bold']));            
            CurrentOrders = [*CurrentOrders, dict(_id=_orderID, order={**Order.get("orderplaced") , "total": Order.get("total")})];
            CartTotal["grand total"] = CartTotal.get("grand total") + Order.get("total");
            print(colored(f"Grand Total so far is: {CartTotal['grand total']}", on_color="on_yellow", attrs=["bold"]));
            CartTotal = {**CartTotal, "all orders": CurrentOrders};
            Budget-= Order.get("total");

            return dict(Budget=Budget, Order=Order, CartTotal=CartTotal);
      except ValueError as err:
           return err;
      except TypeError as err:
           return colored(f"ERROR!!! {err}.", "light_yellow", attrs=["bold"]);



