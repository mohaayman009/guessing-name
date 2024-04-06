import random


def guess():
    a = int(input("Enter first number"))
    b = int(input("Enter second number"))
    num = random.randint(a, b)
    while True:
        myguess = int(input("Enter your guessed number"))
        if myguess == num:
            print("you won!!")
            break

        elif myguess > num:
            print("your guess is higher")
            continue
        else:
            print("your guess os smaller")
            continue


if __name__ == "__main__":
    guess()
