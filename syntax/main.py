import random

hads = ""

javab = random.randint(1, 99)

chances = 5

while hads != str(javab) and chances != 0:
    print(f'answer is : {javab}')
    hads = int(input("what is your guess? ").strip())
    if hads == javab:
        print("You won")
        exit()
    elif hads > javab:
        print("guess smaller ")
        chances -= 1
    else :
        print("guess bigger ")
        chances -= 1
print("You lost")

