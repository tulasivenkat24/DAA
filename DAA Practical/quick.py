import time

# Function to partition the array
def partition(arr, low, high):
    pivot = arr[high]  # Choose the last element as pivot
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Place pivot in the correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Function to perform Quick Sort
def quick_sort(arr, low, high):
    if low < high:
        # Partition the array
        pi = partition(arr, low, high)

        # Recursively sort elements before and after partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

# User Input
n = int(input("Enter the number of elements: "))

arr = []
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

# Record start time
start_time = time.perf_counter()

# Perform Quick Sort
quick_sort(arr, 0, n - 1)

# Record end time
end_time = time.perf_counter()

# Calculate execution time
execution_time = end_time - start_time

# Display Results
print("\nSorted Array:")
print(arr)

print(f"\nExecution Time: {execution_time:.8f} seconds")

print("\nTime Complexity:")
print("Best Case   : O(n log n)")
print("Average Case: O(n log n)")
print("Worst Case  : O(n²)")

print("\nSpace Complexity:")
print("Best/Average: O(log n)")
print("Worst Case  : O(n)")
