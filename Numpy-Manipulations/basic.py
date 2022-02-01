import numpy as np
import pandas as pd

print("problem 1")  # problem 1: Compute the min/max for each row for a NumPy 2D array
np.random.seed(10)

a = np.random.randint(1, 10, [5, 3])  # return random integer from 1 to 10, the size of the array is 5x3

# use apply_along_axis to use a specified function along with !D slices of the input array
solution = np.apply_along_axis(lambda x: np.min(x) / np.max(x), arr=a, axis=1)  # since row so axis =1

print(solution)

print("problem 2")  # problem 2: find all occurrences of an Element in a list
# for list data structure

my_list = [1, 2, 3, 1, 2, 4, 5, 6, 3, 2, 1]

indices = [i for i, x in enumerate(my_list) if
           x == 5]  # iterator enumerate(my_list) yields pairs (index, item) for each item in the list.
print(indices)

values = np.array(my_list)
ii = np.where(values == 5)[0]
print(ii)

print("problem 3")  # problem 3: convert Pandas DataFrame into a Numpy array
df = pd.DataFrame(data={'A': [1, 2, 3],
                        'B': [4, 5, 6],
                        'C': [7, 8, 9]}, index=['a', 'b', 'c'])

# convert the entire dataframe
print(df.to_numpy())

# convert specific clms
print(df[['A', 'C']].to_numpy)
