import random

"""
Merges two sorted lists into one sorted list by comparing their elements. It continues until both lists are fully merged.
"""
def merge(left, right):
    result = []
    i, j = 0, 0  # it uses indices to keep track of the current position in each half
    
    # it used to compare elements from both halves and merge them in sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1  # It used to move to the next element in the left half
        else:
            result.append(right[j])
            j += 1  # It used to move to the next element in the right half
    
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

"""
Generates a list of random integers and sorts it using merge_sort(). Returns the sorted list.
"""
def generate_sorted_data(size):
    data = [random.randint(1, 100) for _ in range(990)]
    sorted_data =merge_sort(data) 
    return sorted_data


def main():
    large_data = [55, 22, 89, 34, 67, 90, 15, 72, 39, 44]
    sort =merge_sort(large_data)
    print(sort)
if __name__ == "__main__":
    main()