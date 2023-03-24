###question 1!!!
###first im trying to make a dict of produce and im going to try to implement that into the class as i saw others do on previous assingments
produce = {"Grapes": 10, "Banana": 10, "Apples": 25, "Potatos": 100, "Eggs": 50, "MEMES": 9000}


class Cart():
    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity):
        """this func is for adding item(s) to the customers cart"""
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def remove_item(self, item, quantity):
        """this func is for removing item(s) from the customer cart"""
        if item in self.items:
            if self.items[item] <= quantity:
                del self.items[item]
            else:
                self.items[item] -= quantity
        else:
            print("Apologies, we were unable to find that item in your current cart.")

    def show_items(self):
        """This function is to show the customer what they have in their current shopping cart."""
        print('Items in your cart are currently: ')
        for item, quantity in self.items.items():
            print(f"{item}, {quantity}")


cart1 = Cart()
cart1.add_item("Potatos", 20)
cart1.add_item("MEMES", 66)
cart1.remove_item("Potatos", 10)
cart1.show_items()



###question 2!!!!
class StringUpper():
    def __init__(self):
        self.string = ""
    
    def get_string(self):
        """gets string from user"""
        self.string = input("Enter a statement or phrase: ")

    def print_string(self):
        print(self.string.upper())



    