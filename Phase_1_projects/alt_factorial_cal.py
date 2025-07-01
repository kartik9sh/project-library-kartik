while True:
    num = input("Factorial of: ")
    result = 1
    try:
        if int(num) < 0:
            print("Enter a valid number")
            continue
        else:
            for i in range(2, int(num) + 1):
                result = result*i
            break
    except ValueError:
        print("Enter a valid number")

print(f"Is: {result}")
