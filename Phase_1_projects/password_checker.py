while True:
    password = input("Check password strength of: ").strip().replace(" ", "")
    length_ok = len(password) >= 8
    upper_ok = any(char.isupper() for char in password)
    digit_ok = any(char.isdigit() for char in password)
    lower_ok = any(char.lower() for char in password)
    symbol_ok = any(c in "!@#$%&*" for c in password)

    if length_ok and upper_ok and digit_ok and lower_ok and symbol_ok:
        print("Strong password")
        break
    else:
        print("weak password")
        if length_ok is False:
            print("password should atleast be 8 characters long")
        if upper_ok is False:
            print("password should atleast contain one upper case")
        if digit_ok is False:
            print("password should atleast contain one digit")
        if lower_ok is False:
            print("password should atleast contain one lower case")
        if symbol_ok is False:
            print("password should atleast contain one symbol")
