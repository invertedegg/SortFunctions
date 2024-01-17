import random as r
from validate import validate

# Globals
arrSize = 100

# Python implementation of merge sort
def mergeSort(arr):
    # base case
    if len(arr) == 1:
        return arr
    arr1 = arr[:len(arr)//2]
    arr2 = arr[len(arr)//2:]
    arrS = []

    arr1 = mergeSort(arr1)
    arr2 = mergeSort(arr2)

    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            arrS.append(arr1[i])
            i += 1
        else:
            arrS.append(arr2[j])
            j += 1
    if(i < len(arr1)):
        for a in arr1[i:]:
            arrS.append(a)
    else:
        for b in arr2[j:]:
            arrS.append(b)
    return(arrS)

def main():
    arr = []
    for x in range (0, arrSize + 1):
        arr.append(r.randint(0, arrSize))
    print(arr)
    sorted = mergeSort(arr)
    print(sorted)
    if validate(sorted):
        print("Merge sort validated")
    else:
        print("Merge sort failed")
    

if __name__ == "__main__":
    main()
