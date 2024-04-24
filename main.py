
# List assignment

women = ["Hannah", "Esther", "Zoe", "Clara", "Olivia"]
print(women)

# Jenny come to the start
women.insert(0, "Jenny")
print(women)

# 3rd woman leaves because of a phone call
women.pop(2) # zero based so 3rd woman is index 2
print(women)

# Alice joins the line 
women.append("Alice")
print(women)
