import time
#Function for bubble sort
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no swaps occurred, the list is already sorted
        if not swapped:
            break

# User Input
n = int(input("Enter the number of elements: "))

arr = []
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

# Record start time
start_time = time.perf_counter()

# Perform Bubble Sort
bubble_sort(arr)

# Record end time
end_time = time.perf_counter()

# Calculate execution time
execution_time = end_time - start_time

# Display Results
print("\nSorted Array:")
print(arr)

print(f"\nExecution Time: {execution_time:.8f} seconds")

print("\nTime Complexity:")
print("Best Case   : O(n)      (Already Sorted)")
print("Average Case: O(n^2)")
print("Worst Case  : O(n^2)")

print("\nSpace Complexity:")
print("O(1)")
