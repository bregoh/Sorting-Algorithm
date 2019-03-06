/**
** This function divides an array and merges it
** params : array
** return : sorted array
**/
function divideArray(arrayList)
{
	/**
	** is the array length greater than 1?
	*/
    if(arrayList.length > 1) 
    {
        const middle = Math.floor(arrayList.length / 2) // get the floor value of the array after division
        const arr1 = arrayList.slice(0, middle) // get the first half / left side of the array
        const arr2 = arrayList.slice(middle) // get the second half or right side of the array

		// output the array
        console.log(arr1)
        console.log(arr2)

        return mergesort(divideArray(arr1), divideArray(arr2)) // return sorted array. See the recursive function used
		// if you do not know a bit of how merge sort works but you are unsure of the coding, you can add print statements on each line to view the steps
    }

    return arrayList
}


function mergesort(array1, array2)
{
    let i = 0
    let j = 0

    let arrayList = [] //initialise an empty array or you could parse the original array

	// check if the length of both sliced array are > n ( n = 0, 1, 2...... array.length)
    while(i < array1.length && j < array2.length)
    {
        if(array1[i] < array2[j]) // compare the values
        {
            arrayList.push(array1[i]) // push the smallest value
            i = i + 1
        }
        else
        {
            arrayList.push(array2[j]) // push the smallest value
            j = j + 1
        }
    }

    return arrayList.concat(array1.slice(i)).concat(array2.slice(j)) // merge the array and return it
}

let arrayL = [10, 14, 19, 26, 27, 31, 33, 35, 42, 44, 0]

console.log(divideArray(arrayL))