import random as r
from validate import validate

#Globals
arrSize = 100

# Function to build an array from the 
# components of the current sorting iteration
def buildArr(arrL, par, arrM):
    arr = []
    if len(arrL) > 0:
        for n in arrL:
            arr.append(n)
    arr.append(par)
    if len(arrM) > 0:
        for n in arrM:
            arr.append(n)
    return arr

# Python implementation of quick sort
def quickSort(arr):
    # base case
    if len(arr) <= 1:
        return arr
    arrL = []
    arrM = []
    partition = arr.pop()
    for v in arr:
        if v <= partition: 
            arrL.append(v)
        else: 
            arrM.append(v)
    arrL = quickSort(arrL)
    arrM = quickSort(arrM)
    return buildArr(arrL, partition, arrM)

def main():
    arr = []
    for x in range (0, arrSize + 1):
        arr.append(r.randint(0, arrSize))
    print(arr)
    sorted = quickSort(arr)
    print(sorted)
    if validate(sorted):
        print("Quick sort validated")
    else:
        print("Quick sort failed")

if __name__ == "__main__":
    main()
