import time

# Function for Selection Sort
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        # Assume the current index has the minimum value
        min_index = i

        # Find the minimum element in the remaining unsorted array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# User Input
n = int(input("Enter the number of elements: "))

arr = []
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

# Record start time
start_time = time.perf_counter()

# Perform Selection Sort
selection_sort(arr)

# Record end time
end_time = time.perf_counter()

# Calculate execution time
execution_time = end_time - start_time

# Display Results
print("\nSorted Array:")
print(arr)

print(f"\nExecution Time: {execution_time:.8f} seconds")

print("\nTime Complexity:")
print("Best Case   : O(n²)")
print("Average Case: O(n²)")
print("Worst Case  : O(n²)")

print("\nSpace Complexity:")
print("O(1)")
