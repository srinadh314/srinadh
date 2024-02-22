class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item, quantity=1):
        self.items.append({"item": item, "quantity": quantity})

    def remove_item(self, item_name):
        self.items = [i for i in self.items if i["item"].name != item_name]

    def calculate_total(self):
        total = sum(item["item"].price * item["quantity"] for item in self.items)
        return total

    def display_order(self):
        print("Order:")
        for item in self.items:
            print(f"{item['item'].name}: {item['quantity']} x ${item['item'].price} = ${item['quantity']*item['item'].price}")
        print(f"Total: ${self.calculate_total()}")

# Example usage:
order = Order()
order.add_item(MenuItem("Pizza", "Classic Margherita", 10), quantity=2)
order.add_item(MenuItem("Pasta", "Spaghetti Carbonara", 12))
order.display_order()

