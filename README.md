# Sorting Functions

A collection of sorting functions, as well as an executable script to validate them, implemented in Python.

Uses an iterative loop to fill an array with random integers, and uses recursive implementations of algorithms to sort them.

## Descriptions
The sorting algorithms implemeted are explained below.

### Merge Sort
The array is initially split into two halves; these halves are then also split into halves until the
array is a single value. Then, the two arrays are compared, index by index, and merged into a separate
array in order from least to greatest. The arrays are sorted in this manner backwards until the initial
split is reached, where the two arrays are merged providing a sorted solution.

### Quick Sort
The array pops off its last index to be used as a partition. Next, the array is broken into two separate
arrays: one contains all values less than the partition, the other contains all values greater than
the partition. These arrays are then sorted using the same method, until the base case of an empty
array or a singular value is reached. Then, the arrays and corresponding partition are rejoined as a
singular array, until the final sorted array is produced and returned.

### Bubble Sort
The array is passed to the sorting function, and the first index is compared to it's neighbor. Of
the two values, the greater one is placed to the right and the lesser one is placed to the left. This
process is then repeated until the end of the array is reached, and the largest unsorted value is at
the end of the array. The function recurses, and the sorting process begins again, until the new largest
unsorted value is placed correctly. This process continues until all values in the array are placed
in their correct positions.
