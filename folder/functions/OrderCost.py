from folder.menu import Menu;
from folder.functions.apis.state_tax_rate import SalesTax;
from folder.restaurant_details import YummyTummyDetails;

def SubTotal(quantity, itemNumber, Menu:list=Menu):
   item = list(filter(lambda x: x[0] == int(itemNumber), Menu))[0];
   CostPerItem = list(item[1].items())[0][1];
   subtotal = float(quantity)*CostPerItem;
   Tip = round(subtotal*0.2, 2); #Added the tip.
   TotalCost = round((subtotal + (subtotal*SalesTax(YummyTummyDetails.get("zip")))) + Tip, 2) #With Tip

   return dict(message='Order placed SUCCESSFULLY!!!', orderplaced= dict(quantity=quantity, item=item[1]), SubTotal=float(subtotal), total=float(TotalCost)) #Logic for each order.