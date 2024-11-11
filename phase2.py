import random

def insertion_sort(array):
    for current_index in range(1, len(array)):
        key_value = array[current_index]
        previous_index = current_index - 1
        while previous_index >= 0 and key_value < array[previous_index]:
            array[previous_index + 1] = array[previous_index]
            previous_index -= 1
        array[previous_index + 1] = key_value
    return array

def generate_sorted_data(size):
    data = [random.randint(1, 100) for _ in range(size)]
    sorted_data = insertion_sort(data) 
    return sorted_data

def binary_search(array, target):

    """
    Initializes two variables, left_index and right_index, which represent the current bounds of the search range.
    left_index starts at 0 (beginning of the array), and right_index starts at the last index (len(array) - 1).
    """
    left_index = 0
    right_index = len(array) - 1
    while left_index <= right_index: #Starts a while loop that continues as long as left_index is less than or equal to right_index.
        middle_index = (left_index + right_index) // 2  #middle_index is the index of the element that will be checked on each iteration.
        if array[middle_index] == target: #Checks if the element at middle_index is equal to the target.
            return middle_index  
        
            """
            If the element at middle_index is less than the target, 
            it means the target must be in the right half of the current range (because the array is sorted).
            """
        elif array[middle_index] < target:
            left_index = middle_index + 1 

            """
            If the element at middle_index is greater than the target, 
            it means the target must be in the left half of the current range.
            """
        else:
            right_index = middle_index - 1  
    return None  

def main():
    small_data = [34, 7, 23, 32, 5, 62, 29, 12, 40, 8]
    print("Original small data:", small_data)
    sorted_small_data = insertion_sort(small_data) #Stores the sorted array in sorted_small_data.
    print("Sorted small data:", sorted_small_data)

    target = 29 #sets target
    found_index = binary_search(sorted_small_data, target)
    print(f"Index of {target} in sorted small data:", found_index)

if __name__ == "__main__":
    main() 