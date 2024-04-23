# This is an example Python program.
# The user inputs a number.
# The program then outputs all the EVEN numbers from 0 to that number.
rangeNum = int(input("Enter the max number you'd like to go up to: \n"))

# We define a for loop that runs from 0 to rangeNum.
for i in range (0, rangeNum):          
  # This checks if the current number of the loop is EVEN.
  if i%2 == 0: 
    print(i)