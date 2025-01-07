from folder.menu import Menu;
from folder.functions.apis.state_tax_rate import SalesTax;

def SubTotal(quantity, itemNumber, Menu:list=Menu):
   item = list(filter(lambda x: x[0] == int(itemNumber), Menu))[0];
   CostPerItem = list(item[1].items())[0][1];
   subtotal = float(quantity)*CostPerItem;
   TotalCost = round(subtotal + (subtotal*SalesTax()), 2);

   return dict(message='Order placed SUCCESSFULLY!!!', orderplaced= dict(quantity=quantity, item=item[1]), SubTotal=float(subtotal), total=float(TotalCost))