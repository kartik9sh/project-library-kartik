text = input("Enter text: ")
vowels = "aeiouAEIOU"
result = ""

for char in text:
    if char not in vowels:
        result += char

print(result)