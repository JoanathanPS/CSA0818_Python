#find the index of the given element in the list
list1= [10, 20, 30, 40, 50]
element = 30

if element in list1:
    print("Index:", list1.index(element))
else:
    print("Element not found")
