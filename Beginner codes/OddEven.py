## Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

##Extras:

##If the number is a multiple of 4, print out a different message.
##Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.


def odd_even(num):
    if num%2 != 0:
        print("Odd number")
    elif num==0:
        print("zero")
    else:
        print("even number")


number = int(input("enter a number: "))

odd_even(number)


def multiple_of_four(num):
    if num%4 == 0:
        print("multiple of four")
    else:
        print("not a multiple of four")

number = int(input("enter a number: "))

multiple_of_four(number)

n = int(input("enter first number: "))
m = int(input("Enter secodnd number: "))

def two_nums(n,m):
    if n%m == 0:
        print("Number divisible")
    else:
        print("number not divisible")


two_nums(n,m)

