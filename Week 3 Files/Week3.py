# Inventory Order Processor

# Task 1: Starting inventory and incoming order queue
inventory = {"Controller": 12, "Headset": 6, "Keyboard": 0, "Mouse": 20, "Webcam": 4}

orders = [
    ["Controller", 5],
    ["Keyboard", 3],
    ["Headset", 9],
    ["Mouse", 15],
    ["Monitor", 2],
    ["Controller", 30]
]

# Task 3 (set up): tracking variables
fulfilled_count = 0
unfulfilled_items = []

# Task 2: Process each order in the queue
for order in orders:
    item_name = order[0]
    requested_qty = order[1]

    if item_name in inventory:
        stock = inventory[item_name]

        if stock >= requested_qty:
            # Full fulfillment
            inventory[item_name] = stock - requested_qty
            fulfilled_count = fulfilled_count + 1
            print("Order fulfilled: " + str(requested_qty) + " x " + item_name)

        elif stock > 0:
            # Partial fulfillment
            remainder = requested_qty - stock
            inventory[item_name] = 0
            unfulfilled_items.append([item_name, remainder])
            print("Partial fulfillment: gave " + str(stock) + " x " + item_name + ", short by " + str(remainder))

        else:
            # Stock is exactly 0
            unfulfilled_items.append([item_name, requested_qty])
            print("Out of stock: " + item_name)

    else:
        # Item key does not exist in inventory
        unfulfilled_items.append([item_name, requested_qty])
        print("Invalid item: " + item_name + " is not in inventory")

# Task 3: End of batch summary report
print()
print("----- END OF BATCH SUMMARY -----")

print()
print("Final inventory levels:")
for key, value in inventory.items():
    print(key + ": " + str(value))

print()
print("Total fully fulfilled orders: " + str(fulfilled_count))

print()
print("Unfulfilled or short items:")
for entry in unfulfilled_items:
    print(entry[0] + " - short by " + str(entry[1]))
