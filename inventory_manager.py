# --- Inventory Management System Pro ---
# Developer: [Your Name]
# Topic: Dictionaries, Functions and CRUD Operations

inventory = {}

def add_item(name, quantity):
    """Adds an item to the inventory or updates its quantity."""
    if name in inventory:
        inventory[name] += quantity
        print(f"🔄 {name} updated. New quantity: {inventory[name]}")
    else:
        inventory[name] = quantity
        print(f"✨ {name} added to inventory.")

def remove_item(name):
    """Safely removes an item from the inventory."""
    if name in inventory:
        inventory.pop(name)
        print(f"🗑️ {name} removed.")
    else:
        print(f"⚠️ Error: {name} not found.")

def display_inventory():
    """Lists all items in the current inventory."""
    print("\n--- 🎒 CURRENT INVENTORY ---")
    if not inventory:
        print("Bag is empty.")
    else:
        for item, quantity in inventory.items():
            print(f"- {item}: {quantity}")
    print("-------------------------")

def main():
    while True:
        print("\n1- Add | 2- Remove | 3- List | Q- Exit")
        choice = input("Select an action: ").lower()

        if choice == "1":
            name = input("Item name: ")
            qty = int(input("Quantity: "))
            add_item(name, qty)
        elif choice == "2":
            name = input("Item name to remove: ")
            remove_item(name)
        elif choice == "3":
            display_inventory()
        elif choice == "q":
            print("Exiting system... Goodbye!")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()
