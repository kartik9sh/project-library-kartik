num = int(input("Enter a number: "))
start = int(input("start? : "))
end = int(input("end? :")) + 1
userinput = input("want output reverse order? ").strip().lower()
if userinput == "no":
    for i in range(start, end):
        print(f"{num} x {i} = {num * i}")
if userinput == "yes":
    for i in range(start, end):
        I = end - i - 1 + start
        print(f"{num} x {I} = {num * I}")

# I specifically created it such that the outputs are in reversed order
