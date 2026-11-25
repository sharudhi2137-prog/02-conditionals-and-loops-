number = int(input("Enter a number: "))

reverse = 0
temp = number

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

print("Reversed number:", reverse)

Output
Reversed number: 54321
