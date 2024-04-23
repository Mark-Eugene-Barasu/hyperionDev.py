
# Info collector
userName = input("Please enter for full name: ")
userGender = input("please chose M or F to identify your gender : ")
userAge = input("How old are you? : ")
userHouseAddress = input("What is your house number? : ")
userStreetName = input("Enter street name : ")
if(userGender == "M" or userGender == "m"):
    userGender = "he"
else:
    userGender = "she"

print(f"This is {userName}, {userGender} is {userAge} years old and live at {userHouseAddress} {userStreetName}")


