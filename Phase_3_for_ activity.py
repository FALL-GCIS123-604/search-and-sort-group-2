import random
def merge(first_half, second_half):
    result = []
    i, j = 0, 0  # it uses indices to keep track of the current position in each half
    
    # it used to compare elements from both halves and merge them in sorted order
    while i < len(first_half) and j < len(second_half):
        if first_half[i] < second_half[j]:
            result.append(first_half[i])
            i += 1  # It used to move to the next element in the left half
        else:
            result.append(second_half[j])
            j += 1  # It used to move to the next element in the right half
    
    # Add any remaining elements from the left or right part
    result.extend(first_half[i:])
    result.extend(second_half[j:])
    
    return result

def merge_sort(array):
    if len(array) <= 1:
        return array
    
    # to split the array into even-indexed and odd-indexed elements
    left_half = array[::2]  # Even indices like (0, 2, 4)
    right_half = array[1::2]  # Odd indices like (1, 3, 5)
    
    # Recursively sort both halves
    sorted_even = merge_sort(left_half)
    sorted_odd = merge_sort(right_half)
    
    # Merge the sorted halves using the merge function
    return merge(sorted_even, sorted_odd)



def generate_sorted_data(size):
    # Initial array to be sorted
    initial_array = [55, 22, 89, 34, 67, 90, 15, 72, 39, 44]
    
    # Sort the initial data
    sorted_initial_data = merge_sort(initial_array)
    
    # Generate random numbers for the remaining elements
    random_data = [random.randint(1, 100) for _ in range(size - 10)]
    
    
    # Combine the sorted initial data with the sorted random data
    combined_data = sorted_initial_data + random_data
    return combined_data

# Generate the sorted data with a total of 1000 elements
sorted_large_data = generate_sorted_data(1000)
print(sorted_large_data)