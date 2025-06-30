while True:
    num = input("Whats the number? : ").strip()
    if not (num.strip("+-").isdigit()):
        print("Invalid input. Please enter a valid number.")
        continue
    if int(num) == 0:
        print("Invalid input. Please enter a valid number.")
        continue
    if num.startswith("-"):
        num = int(num.strip("-"))
        if num % 2 == 1:
            print("Negative Odd")
        else:
            print("Negative Even")
    else:
        num = int(num.strip("+"))
        if num % 2 == 1:
            print("Positive Odd")
        else:
            print("Positive Even")

    break
