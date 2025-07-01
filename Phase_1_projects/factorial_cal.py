while True:
    num = input("Factorial of: ")
    result = 1
    if not (num.strip("+").isdigit()):
        print("Enter a valid number")
        continue
    elif int(num) < 0:
        print("Enter a valid number")
        continue
    else:
        for i in range(2, int(num) + 1):
            result = result*i
        break

print(f"Is: {result}")
