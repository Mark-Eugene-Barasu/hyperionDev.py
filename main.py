
# List method assignment

animals = ["Elephant", "Giraffe", "Dog", "Cat"]

# remove the second animal in the list
hold = animals.pop(1)
print(f"{hold} of was taken out of {animals} ")

# add cheetah to the list
animals.insert(50, "cheetah")
print(animals)

# remove cheetah from the list
animals.remove("cheetah")
print(animals)
