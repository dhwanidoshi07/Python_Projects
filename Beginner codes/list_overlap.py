"""
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

Extras:

Randomly generate two lists to test this
Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

"""


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 3, 4, 8, 9]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1,21, 34, 55, 89, 3, 4, 8, 9]

if len(a) > len(b):
    lst1 = list(a)
    lst2 = list(b)
else:
    lst1 = list(b)
    lst2 = list(a)


def overlap(a,b):
    result = []
    for i in a:
        for j in b:
            if i == j and i not in result:
                result.append(i)
    return result

result = overlap(lst1,lst2)
print(result)



    
