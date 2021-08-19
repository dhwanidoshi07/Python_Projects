"""
Make a two-player Rock-Paper-Scissors game. 
(Hint: Ask for player plays (using input), compare them, 
print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock

"""

user1 = int(input("Enter your choice: 1. Rock, 2. Scissors, 3.Paper 0.exit  "))
user2 = int(input("Enter your choice: 1. Rock, 2. Scissors, 3.Paper 0.exit  "))

flag = 1
def compare(a,b):
    while(flag == 1):
        if a == 0 or b == 0:
            flag == 0
            print("game over")
            break
        elif a == b:
            print("tied")
            break
        elif a == 1:
            if b == 2:
                print("user 1 wins")
                break
            else:
                print("user 2 wins")
                break
        elif a==2:
            if b == 3:
                print("user 1 wins")
                break
            else:
                print("user 2 wins")
                break
        elif a==3:
            if b == 1:
                print("user 1 wins")
                break
            else:
                print("user 2 wins")
                break
        else:
            print("invalid input")
            break

compare(user1,user2)
    
        

    
