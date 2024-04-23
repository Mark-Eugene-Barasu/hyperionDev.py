
# Slicing multiple characters in a string.

print("Example 1:")

veryLongWord = "supercalifragilisticexpialidocious"
print(veryLongWord[0:5]) # super

print("Example 2:")
index = 6 # just a variable
print(veryLongWord[index:9]) # ali

print("Example 3:")
print(veryLongWord[0::]) # supercalifragilisticexpialidocious
print(veryLongWord[::]) # supercalifragilisticexpialidocious
print(veryLongWord[:9]) # supercali
