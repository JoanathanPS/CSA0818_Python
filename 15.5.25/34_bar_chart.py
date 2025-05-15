import matplotlib.pyplot as plt

products = ['A', 'B', 'C', 'D']
sales = [40, 60, 80, 100]

plt.bar(products, sales, color='skyblue')
plt.title('Product Sales')
plt.xlabel('Products')
plt.ylabel('Sales')
plt.show()