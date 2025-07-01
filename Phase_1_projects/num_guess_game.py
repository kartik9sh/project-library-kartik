import random
secret_num = random.randint(1, 100)
tries = 0
guess = None

while guess != secret_num:
    guess = int(input("Guess the secret number between (1,100): "))
    tries = tries + 1
    if tries == 7:
        print("you lost")
        break
    elif guess < secret_num:
        print("too low")
    elif guess > secret_num:
        print("too high")
    else:
        print(f"you took {tries} tries, you won!")
        break


