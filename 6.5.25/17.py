#Remove the duplicates from given list
input_list = [1, 2, 2, 3, 1, 4, 5]
unique_list = []
for i in input_list:
    if i not in unique_list:
        unique_list.append(i)
print("List without duplicates:", unique_list)
