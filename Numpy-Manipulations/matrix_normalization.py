import numpy as np

mylist = np.array(
    [[1, 2, 0],
     [0, 1, 1],
     [5, 6, 5]])


# regular normalization
# norm = np.linalg.norm(mylist)

# #normalize the array
# norm_mylist = mylist/norm
# print(norm_mylist)

# mean of each clm
cmean = mylist.mean(axis=0)

#stdev of each clm
cstdev = np.std(mylist, axis=0)

#normalized matrix -- formula shared in the problem
result = (mylist-cmean)/cstdev
print(result)

#mean of each clm of the normalized matrix should be 0
print(result.mean(axis=0))

#std of each clm of the normalized matrix should be 1
print(np.std(result, axis=0))