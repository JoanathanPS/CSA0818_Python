n = int(input("Enter the value of n: "))
sum_squares = 0
for i in range(1, n + 1):
    sum_squares += i * i
print("Sum of squares of the first", n, "natural numbers is:", sum_squares)