"""

Ask the user for a string and print out whether this string is a palindrome or not. 
(A palindrome is a string that reads the same forwards and backwards.)

"""

string = str(input("Enter string: "))

def reverse(string):
    string = string[::-1]
    return string

string2 = reverse(string)

string.islower()
string2.islower()

if string == string2:
    print('yes')
else:
    print("no")