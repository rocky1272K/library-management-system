from datetime import datetime

class Supermarket:
    def __init__(self):
        self.inventory = {}
        self.cart = {}
        self.initialize_inventory()

    def initialize_inventory(self):
        products = [
            (101, "Apples", 150, 50, "Fruits"),
            (102, "Bananas", 40, 75, "Fruits"),
            (103, "Carrots", 60, 60, "Vegetables"),
            (201, "Milk", 65, 40, "Dairy"),
            (202, "Paneer", 85, 35, "Dairy"),
            (301, "Bread", 35, 30, "Bakery"),
            (401, "Rice", 70, 40, "Grains"),
        ]
        for pid, name, price, qty, cat in products:
            self.inventory[pid] = (name, price, qty, cat)

    def add_item(self, pid, name, price, qty, cat):
        if pid in self.inventory:
            _, _, old_qty, _ = self.inventory[pid]
            self.inventory[pid] = (name, price, old_qty + qty, cat)
        else:
            self.inventory[pid] = (name, price, qty, cat)

    def display_inventory(self):
        for pid, (name, price, qty, cat) in self.inventory.items():
            print(f"{pid}: {name} | ₹{price} | Qty: {qty} | {cat}")

    def search_product(self, term):
        for pid, (name, price, qty, cat) in self.inventory.items():
            if term.lower() in name.lower():
                print(f"{pid}: {name} | ₹{price} | Qty: {qty} | {cat}")

    def add_to_cart(self, pid, qty):
        if pid in self.inventory:
            name, price, stock, cat = self.inventory[pid]
            if qty <= stock:
                if pid in self.cart:
                    _, p, q, c = self.cart[pid]
                    self.cart[pid] = (name, p, q + qty, cat)
                else:
                    self.cart[pid] = (name, price, qty, cat)

    def modify_cart(self, pid):
        if pid in self.cart:
            try:
                new_qty = int(input("New Quantity: "))
                if new_qty > 0 and new_qty <= self.inventory[pid][2]:
                    name, price, _, cat = self.cart[pid]
                    self.cart[pid] = (name, price, new_qty, cat)
            except: pass

    def remove_from_cart(self, pid):
        if pid in self.cart:
            del self.cart[pid]

    def view_cart(self):
        total = 0
        for pid, (name, price, qty, cat) in self.cart.items():
            subtotal = price * qty
            total += subtotal
            print(f"{pid}: {name} | ₹{price} x {qty} = ₹{subtotal} | {cat}")
        print(f"Total: ₹{total}")

    def checkout(self):
        if not self.cart:
            return

        total = 0
        for pid, (name, price, qty, cat) in self.cart.items():
            subtotal = price * qty
            total += subtotal
            n, p, stock, c = self.inventory[pid]
            self.inventory[pid] = (n, p, stock - qty, c)

        gst = total * 0.05
        discount = total * 0.10 if total >= 500 else 0
        grand_total = total + gst - discount

        print("\n===== BILL =====")
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        for pid, (name, price, qty, cat) in self.cart.items():
            print(f"{name} ({qty} x ₹{price}) - ₹{price * qty}")
        print(f"Subtotal: ₹{total:.2f}")
        print(f"GST (5%): ₹{gst:.2f}")
        if discount:
            print(f"Discount (10%): -₹{discount:.2f}")
        print(f"Grand Total: ₹{grand_total:.2f}")
        print("Thank you for shopping!\n")

        self.cart.clear()


def launch_supermarket():
    market = Supermarket()

    while True:
        print("\n1. Admin\n2. Customer\n3. Exit")
        role = input("Choose: ")

        if role == "1":
            while True:
                print("\n--- Admin ---\n1. Add Item\n2. View Inventory\n3. Search\n4. Back")
                ch = input("Choice: ")
                if ch == "1":
                    while True:
                        try:
                            pid = int(input("ID: "))
                            name = input("Name: ")
                            price = float(input("Price: ₹"))
                            qty = int(input("Qty: "))
                            cat = input("Category: ")
                            market.add_item(pid, name, price, qty, cat)
                            more = input("Add another item? (yes/no): ").lower()
                            if more != "yes":
                                break
                        except: pass
                elif ch == "2":
                    market.display_inventory()
                elif ch == "3":
                    market.search_product(input("Search: "))
                elif ch == "4":
                    break

        elif role == "2":
            while True:
                print("\n--- Customer ---\n1. View Inventory\n2. Add to Cart\n3. Modify Cart\n4. Remove\n5. View Cart\n6. Checkout\n7. Search\n8. Back")
                ch = input("Choice: ")
                if ch == "1":
                    market.display_inventory()
                elif ch == "2":
                    while True:
                        try:
                            pid = int(input("ID: "))
                            qty = int(input("Qty: "))
                            market.add_to_cart(pid, qty)
                            more = input("Add another item to cart? (yes/no): ").lower()
                            if more != "yes":
                                break
                        except: pass
                elif ch == "3":
                    try:
                        market.modify_cart(int(input("ID: ")))
                    except: pass
                elif ch == "4":
                    try:
                        market.remove_from_cart(int(input("ID: ")))
                    except: pass
                elif ch == "5":
                    market.view_cart()
                elif ch == "6":
                    market.checkout()
                elif ch == "7":
                    market.search_product(input("Search: "))
                elif ch == "8":
                    break

        elif role == "3":
            break



# if __name__ == "__main__":
launch_supermarket()
