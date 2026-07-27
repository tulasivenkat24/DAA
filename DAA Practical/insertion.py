import time

# Function for Insertion Sort
def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # Move elements greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

# User Input
n = int(input("Enter the number of elements: "))

arr = []
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

# Record start time
start_time = time.perf_counter()

# Perform Insertion Sort
insertion_sort(arr)

# Record end time
end_time = time.perf_counter()

# Calculate execution time
execution_time = end_time - start_time

# Display Results
print("\nSorted Array:")
print(arr)

print(f"\nExecution Time: {execution_time:.8f} seconds")

print("\nTime Complexity:")
print("Best Case   : O(n)")
print("Average Case: O(n²)")
print("Worst Case  : O(n²)")

print("\nSpace Complexity:")
print("O(1)")

