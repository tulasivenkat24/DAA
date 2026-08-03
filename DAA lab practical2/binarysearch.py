import time

# Function for Binary Search
def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# User Input
n = int(input("Enter the number of elements: "))

print("Enter the elements in sorted order:")
arr = []
for i in range(n):
    arr.append(int(input()))

key = int(input("Enter the element to search: "))

# Measure execution time
start_time = time.perf_counter()

result = binary_search(arr, key)

end_time = time.perf_counter()

# Output
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")

print(f"Execution Time: {end_time - start_time:.10f} seconds")