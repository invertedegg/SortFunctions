import random as r
from validate import validate

#Globals
arrSize = 10

# Python implementation of quick sort
def quickSort(arr):
    # base case
    if len(arr) <= 1:
        print("base")
        return arr
    arrL = []
    arrM = []
    partition = arr.pop()
    print(partition)
    for v in arr:
        if v <= partition: 
            arrL.append(v)
        else: 
            arrM.append(v)
    print("arrL: ", arrL)
    print("arrM: ", arrM)
    arrL = quickSort(arrL)
    arrM = quickSort(arrM)
    return [arrL, partition, arrM]

def main():
    arr = []
    for x in range (0, arrSize + 1):
        arr.append(r.randint(0, arrSize))
    print(arr)
    sorted = quickSort(arr)
    print(sorted)
    if validate(sorted):
        print("Merge sort validated")
    else:
        print("Merge sort failed")

if __name__ == "__main__":
    main()
