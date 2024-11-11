import random
import time

# Merge and Merge Sort Functions
"""
Merges two sorted lists into one sorted list by comparing their elements. It continues until both lists are fully merged.
"""
def merge(left, right):
    result = []
    i, j = 0, 0  # Indices to keep track of the current position in each half
    
    # Compare elements from both halves and merge them in sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Append any remaining elements from either half
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

"""
Recursively splits an array into halves and sorts each half. It then merges the sorted halves back together using the merge() function.
"""
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Split the array into even-indexed and odd-indexed elements
    left_half = arr[::2]  # Even indices like (0, 2, 4)
    right_half = arr[1::2]  # Odd indices like (1, 3, 5)
    
    # Recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    
    # Merge the sorted halves using the merge function
    return merge(left_sorted, right_sorted)

# Linear Search Function
"""
Iterates through the array and returns the index of the target if found. Returns None if the target is not in the array.
"""
def linear_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return None

# Binary Search Function
"""
Performs binary search on a sorted array by repeatedly dividing the search range in half. Returns the index of the target if found, or None if not.
"""
def binary_search(array, target):
    left_index = 0
    right_index = len(array) - 1
    while left_index <= right_index:
        middle_index = (left_index + right_index) // 2
        if array[middle_index] == target:
            return middle_index
        elif array[middle_index] < target:
            left_index = middle_index + 1
        else:
            right_index = middle_index - 1
    return None

# Generate Sorted Data Function
"""
Generates a list of random integers and sorts it using merge_sort(). Returns the sorted list.
"""
def generate_sorted_data(size):
    data = [random.randint(1, 100) for _ in range(size)]
    sorted_data = merge_sort(data)  # Use merge sort to sort the data
    return sorted_data

# Main Function with Timing
def main():
    # Generate a sorted dataset
    sorted_data = generate_sorted_data(1000)  # Adjust size for large dataset
    target = 72  # Sample target
    
    # Time Linear Search
    start_time = time.perf_counter()
    linear_time = time.perf_counter() - start_time
    print("Time elapsed for linear search: ",str(linear_time)," seconds")
    
    # Time Binary Search
    start_time = time.perf_counter()
    binary_time = time.perf_counter() - start_time
    print("Time elapsed for binary search: ", str(binary_time)," seconds")

if __name__ == "__main__":
    main()
