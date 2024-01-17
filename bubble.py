import random as r
from validate import validate

# Globals
arrSize = 100

# Python implementation of bubble sort
def bubbleSort(arr, idx):
    # base case
    if idx == 0:
        return arr
    
    place = 0
    while place < idx:
        if arr[place] > arr[place+1]:
            # Swap integer
            temp = arr[place+1]
            arr[place+1] = arr[place]
            arr[place] = temp
        place += 1
    # Completed a pass-through, recurse
    return bubbleSort(arr, idx - 1)

def main():
    arr = []
    for x in range (0, arrSize + 1):
        arr.append(r.randint(0, arrSize))
    print(arr)
    sorted = bubbleSort(arr, len(arr) - 1)
    print(sorted)
    if validate(sorted):
        print("Bubble sort validated")
    else:
        print("Bubble sort failed")

if __name__ == "__main__":
    main()
