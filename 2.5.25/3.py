num = int(input("Enter a number: "))
original_num = num
reversed_num = 0
while num > 0:
    remainder = num % 10
    reversed_num = reversed_num * 10 + remainder
    num = num // 10

if original_num == reversed_num:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")