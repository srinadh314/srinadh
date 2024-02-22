class MenuItem:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

class Restaurant:
    def __init__(self):
        self.menu = []

    def add_menu_item(self, item):
        self.menu.append(item)

    def remove_menu_item(self, item_name):
        self.menu = [i for i in self.menu if i.name != item_name]

    def display_menu(self):
        print("Menu:")
        for item in self.menu:
            print(f"{item.name}: {item.description} - ${item.price}")

# Example usage:
restaurant = Restaurant()
restaurant.add_menu_item(MenuItem("Pizza", "Classic Margherita", 10))
restaurant.add_menu_item(MenuItem("Pasta", "Spaghetti Carbonara", 12))
restaurant.display_menu()
