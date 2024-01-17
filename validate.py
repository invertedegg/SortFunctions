# Validation function
def validate(arr):
    count = 0
    while count + 1 < len(arr):
        if arr[count] > arr[count+1]: return False
        count += 1
    return True