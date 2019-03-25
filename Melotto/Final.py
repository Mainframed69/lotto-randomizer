#More efficient code and exports all permutations to ".csv" & "txt" via numpy array.

import numpy as np
from itertools import combinations


def rSubset(arr, r):
    # return list of all subsets of length r
    # to deal with duplicate subsets use
    # set(list(combinations(arr, r)))
    return list(combinations(arr, r))


#x = bool([1 >= 28])
# Driver Function
if __name__ == "__main__":
    arr = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18 , 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
    r = 3
    print(rSubset(arr, r))

np.array = rSubset(arr, r)
np.savetxt('resultados.csv', np.array, fmt="%s")
np.savetxt('resultados.txt', np.array, fmt="%s")
