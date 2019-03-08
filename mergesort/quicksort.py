import math

# array = array to be sorted
# low = start index of the array
# high = end index of the array


def quicksort(array, low, high):
    if low < high:
        # return the index of the small element
        partition_value = partition(array, low, high)
        # recursive method to sort array before and after partition
        quicksort(array, low, partition_value - 1)
        quicksort(array, partition_value + 1, high)


def partition(array, low, high):
    small_element = (low - 1)
    middle_value = array[high]
    print("new array", array)
    for i in range(low, high):
        print("array[i] is : ", array[i])
        print("middle value is :", middle_value)
        if array[i] <= middle_value:
            print(array[i], " <= ", middle_value)
            # swap the smallest value
            small_element += 1
            temp = array[small_element]
            array[small_element] = array[i]
            array[i] = temp
            print(array)
    # swap the element
    print("swaping array[", small_element + 1, "] with array[", high, "]")
    temp2 = array[small_element + 1]
    array[small_element + 1] = array[high]
    array[high] = temp2
    print("small element is : ", small_element + 1)
    #print(array)
    return small_element + 1


array_to_be_sorted = [10, 7, 8, 9, 1, 5]
length = len(array_to_be_sorted)
quicksort(array_to_be_sorted, 0, length - 1)
print(array_to_be_sorted)
