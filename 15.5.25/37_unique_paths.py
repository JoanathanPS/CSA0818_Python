import math

def unique_paths(m, n):
    return math.comb(m + n - 2, n - 1)

print("Unique paths for m=7, n=3:", unique_paths(7, 3))
print("Unique paths for m=3, n=2:", unique_paths(3, 2))