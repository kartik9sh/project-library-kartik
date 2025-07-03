numbers = [15, 4, 67, 23, 99, 1]
max_num = 0
for num in numbers:

#can also use : basically update the value when greater number is found
#   if num > max_num:
#       max_num = num

    if num > max_num:
        max_num = max_num + num - max_num
    elif num < max_num:
        max_num += 0


print(f"maximum number is: {max_num}")
