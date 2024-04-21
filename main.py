
# import sys

USER_INPUT = int(input("What number will you want the square of? : "))

def square_it(USER_INPUT):
    USER_INPUT *= USER_INPUT
    return USER_INPUT

print("Square of "+ str(USER_INPUT) + " will be "+ str(square_it(USER_INPUT)))
# print(sys.version)
