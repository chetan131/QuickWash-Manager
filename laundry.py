import datetime

# A dictionary to store laundry prices per item
PRICES = {
    "shirt": 5,
    "pants": 7,
    "jacket": 10,
    "towel": 3,
    "bedsheet": 8
}

# A list to store orders
orders = []

# Function to add a new order
def add_order():
    order_id = len(orders) + 1
    customer_name = input("Enter customer name: ")
    items = {}
    while True:
        item = input("Enter item (shirt/pants/jacket/towel/bedsheet) or 'done' to finish: ").lower()
        if item == 'done':
            break
        if item in PRICES:
            quantity = int(input(f"Enter quantity of {item}: "))
            items[item] = items.get(item, 0) + quantity
        else:
            print("Invalid item. Please enter a valid laundry item.")
    
    total_cost = calculate_total_cost(items)
    order = {
        "id": order_id,
        "customer_name": customer_name,
        "items": items,
        "total_cost": total_cost,
        "status": "Pending",
        "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    orders.append(order)
    print(f"Order added successfully! Order ID: {order_id}")

# Function to calculate the total cost of an order
def calculate_total_cost(items):
    total_cost = 0
    for item, quantity in items.items():
        total_cost += PRICES[item] * quantity
    return total_cost

# Function to update order status
def update_order_status():
    order_id = int(input("Enter order ID to update: "))
    for order in orders:
        if order['id'] == order_id:
            new_status = input("Enter new status (Pending/In Progress/Completed): ")
            if new_status in ["Pending", "In Progress", "Completed"]:
                order['status'] = new_status
                print("Order status updated successfully!")
            else:
                print("Invalid status. Please enter a valid status.")
            return
    print("Order not found.")

# Function to display all orders
def display_orders():
    if not orders:
        print("No orders to display.")
        return

    print("\n--- Laundry Orders ---")
    for order in orders:
        print(f"\nOrder ID: {order['id']}")
        print(f"Customer Name: {order['customer_name']}")
        print(f"Order Date: {order['date']}")
        print(f"Items: {order['items']}")
        print(f"Total Cost: ${order['total_cost']}")
        print(f"Status: {order['status']}")
        print("----------------------------")

# Main function to run the app
def main():
    while True:
        print("\nLaundry Service Menu:")
        print("1. Add a new order")
        print("2. Update order status")
        print("3. Display all orders")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_order()
        elif choice == '2':
            update_order_status()
        elif choice == '3':
            display_orders()
        elif choice == '4':
            print("Thank you for using the Laundry Service App!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
