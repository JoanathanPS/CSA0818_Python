start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print("Ascending order:")
for i in range(start, end + 1):
    print(i, end=" ")

print("\nDescending order:")
for i in range(end, start - 1, -1):
    print(i, end=" ")