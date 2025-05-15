import pandas as pd
import numpy as np

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Salary': np.random.randint(5000, 99000, size=4)}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
print("\nFiltered (Salary > 50000):")
print(df[df['Salary'] > 50000])