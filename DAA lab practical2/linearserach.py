import time

# Function for Linear Search
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

# User Input
n = int(input("Enter the number of elements: "))

arr = []
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

key = int(input("Enter the element to search: "))

# Measure execution time
start_time = time.perf_counter()

result = linear_search(arr, key)

end_time = time.perf_counter()

# Output
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")

print(f"Execution Time: {end_time - start_time:.10f} seconds")