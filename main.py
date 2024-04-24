
# initializing and assigning variables
keep = 0 # values from input
adding = 0 # for adding of inputs
count = 0 # iterate each loop 

while keep != -1: # (0 != -1) == true just to kick start loop
    count += 1 # increment by 1
    keep = float(input("enter number please : ")) # get input
    adding += keep # add every input

adding += 1 # plus one to counter oppose the last number of -1 to end the loop
count -= 1 # deducted one to exclude the last count with the value -1
average = adding / count # calculate average
print(f"average is {average}") #print average

# I really enjoyed this assignment. It really rocked my brain a bit :)
