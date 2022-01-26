import numpy as np

mylist = np.array(
    [[1, 2, 0],
     [0, 1, 1],
     [5, 6, 5]])

# print(mylist)

# calculate mean for clm values; for rows axis=1
clm_mean = mylist.mean(axis=0)
# print(clm_mean)

row_mean = mylist.mean(axis=1)
# print(row_mean)

# calculate mean of non-zero clm values
# clm_mean1 = np.true_divide(mylist.sum(0),(mylist!=0).sum(0))
# print(clm_mean1)

# replaces 0 with 100;
# mylist = np.where((mylist == 0),100,mylist)
# print(mylist)

#replaces 0 with mean;
# mylist = np.where((mylist == 0),mylist.mean(axis=0),mylist)
# # print(mylist)

# replaces 0 with non-zero mean of the clm values;
mylist = np.where((mylist == 0), np.true_divide(mylist.sum(0), (mylist != 0).sum(0)), mylist)
print(mylist)