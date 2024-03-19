class Inventory:
    def __init__(self):
        self.inventory = []

    def add_item(self):
        new_item = {'name': input("What item would you like to add?: \n").lower(),
                    'amount': int(input("How many?: \n"))
                    }
        self.inventory.append(new_item)

    def display_inventory(self):
        for item_dict in self.inventory:
            for k, v in item_dict.items():
                print(f"{k}:{v}", end='|')
            print()

    def remove_item(self) :
        remove_item = input("Which item would you like to remove?: \n")
        remove_amount = int(input("How many would you like to remove?: \n"))

        new_inventory = []
        item_removed = False

        for item in self.inventory:
            if item['name'] == remove_item:
                item['amount'] -= remove_amount
                if item['amount'] <= 0:
                    print(f"No {item['name']}'s left, {item['name']} is removed from Inventory")
                else:
                    new_inventory.append(item)
                    print(f"{remove_amount} removed from {item['name']} in inventory")
                item_removed = True
            else:
                new_inventory.append(item)

        if not item_removed:
            print('Item not in inventory')

        self.inventory = new_inventory