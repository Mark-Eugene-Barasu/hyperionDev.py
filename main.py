
# List methods
groceries = ["apples", "milk", "cheese", "bread"]
# groceries.append("coffee") # ["apples", "milk", "cheese", "bread"]
# groceries.insert(len(groceries), "carrots") #["apples", "milk", "cheese", "bread", "coffee"]
print(groceries)
print(groceries.append("coffee") == groceries.insert(len(groceries), "coffee"))

