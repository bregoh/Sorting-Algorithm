import math

################################################
## This function divides an array and merges it
## params : array, the first index, last index
## return : sorted array
################################################

def divideArray(arrayList, start, length):

	## check if the first index > last index
    if start < length:
        arraylength = len(arrayList)
        #print("array length", arraylength)
        middle = math.floor(arraylength // 2)
        #print("middle ", middle)
        array1 = arrayList[:middle] # get the first half / left side of the array by slicing the array
        array2 = arrayList[middle:] # get the second half or right side of the array by slicing the array
        divideArray(array1,start, middle) # recursion used to continually devide the array to 2 single arrray
        divideArray(array2,middle + 1, arraylength) # recursion used to continually devide the array to 2 single arrray
        mergesort(arrayList, array1, array2) #// return sorted array. See the recursive function used
		# if you do not know a bit of how merge sort works but you are unsure of the coding, you can add print statements on each line to view the steps


def mergesort(arrayList, array1, array2):
    i = 0
    j = 0
    k = 0

    #print("Original array is ", arrayList)
    #print("Left array is ", array1)
    #print("Right array is ", array2)

	# check if the length of both sliced array are > n ( n = 0, 1, 2...... array.length)
    while i < len(array1) and j < len(array2):
        if array1[i] <= array2[j]:
            arrayList[k] = array1[i] #swap the current value with the smallest value
            i = i + 1
            #print("Unsorted - 1 ", arrayList)
        else:
            arrayList[k] = array2[j] #swap the current value with the smallest value
            j = j + 1
            #print("Unsorted - 2 ", arrayList)
        k = k + 1
        #print("Unsorted ",arrayList)

	# check if the length of both sliced array are > n ( n = 0, 1, 2...... array.length)
    while i < len(array1):
        arrayList[k] = array1[i]
        i = i + 1
        k = k + 1

    while j < len(array2):
        arrayList[k] = array2[j]
        j = j + 1
        k = k + 1
    #print(arrayList)

arrll = [10, 14, 19, 26, 27, 31, 33, 35, 42, 44, 0]
divideArray(arrll, 0, len(arrll))
print(arrll)

