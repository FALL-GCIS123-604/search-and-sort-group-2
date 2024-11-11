import random

"""
Defines a function called insertion_sort and takes an array as an argument.
The function will sort this array in ascending order using the insertion sort algorithm.
"""
def insertion_sort(array):

    """
A for loop with current_index starting from 1 up to the last index of array.
This loop iterates through each element in the array starting from the second element.
"""
    for current_index in range(1, len(array)):

        """
        key_value is set to the value of the element at current_index.
        This is the value that needs to be inserted into the sorted portion of the array.
        """
        key_value = array[current_index]

        """
        previous_index is initialized to the index immediately before current_index,
        which represents the last element of the sorted portion.
        """
        previous_index = current_index - 1

        """
        A while loop is used to move elements of the sorted portion of the array one position to the right if they are larger than key_value.
        This loop continues as long as previous_index is within bounds (>= 0) and the element at previous_index is greater than key_value.
        Inside the while loop, the element at previous_index is moved one position to the right.
        This creates space for key_value in the correct sorted position.
        """
        while previous_index >= 0 and key_value < array[previous_index]:
            array[previous_index + 1] = array[previous_index]
            previous_index -= 1 #Decreases previous_index by 1, moving left in the array to continue
        array[previous_index + 1] = key_value #the portion of the array from the beginning to current_index is sorted.
    return array

"""
This function generates an array of random integers and sorts it using insertion_sort.
Generates a list of random integers between 1 and 100, with size elements.
"""
def generate_sorted_data(size):
    data = [random.randint(1, 100) for _ in range(size)]
    sorted_data = insertion_sort(data) 
    return sorted_data

def main():
    """
    Defines a list small_data with specific integers to demonstrate sorting.
    """
    small_data = [34, 7, 23, 32, 5, 62, 29, 12, 40, 8] 
    print("Original small data:", small_data) #Prints the original, unsorted small_data array.
    sorted_small_data = insertion_sort(small_data) #Calls insertion_sort on small_data to get a sorted version
    print("Sorted small data:", sorted_small_data) #Prints the sorted version of small_data

if __name__ == "__main__":
    main()