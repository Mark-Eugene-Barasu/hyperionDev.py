
# if statement

current_hour = 22
guards_presence = False

if ((current_hour >= 7) and (current_hour <= 17)):
    print("You're in")
elif ((current_hour < 7 and guards_presence == True) or (current_hour > 17 and guards_presence == True)):
    print("You're in")
else:
    print("Sorry, Try another day.")


# great assignment on if elif and else statement
