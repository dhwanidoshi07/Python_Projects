#Take a list, say for example this one:

  #a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#and write a program that prints out all the elements of the list that are less than 5.

#Extras:

#Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
#Write this in one line of Python.
#Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.

lst = [23,1,3,54,6,2,43,1,3,7,2,1,4,23,44,23,87,67,566,98,23,1,2,4,5]

def less_than_5(lst):
  result = []
  for i in lst:
    if i<=5:
      result.append(i)

  return result

#new = less_than_5(lst)
#print(new)


#using list comprehension
#result = [i for i in lst if i<=5]
#print(result)

def less_than_num(lst,num):
  result = []
  for i in lst:
    if i<=num:
      result.append(i)

  return result


num = int(input("Enter number: "))
f = less_than_num(lst,num)
print(f)



