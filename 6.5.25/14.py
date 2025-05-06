input_list = [1, 2, 2, 3, 1, 4, 2]
frequency = {}

for item in input_list:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

print("Frequencies:", frequency)
