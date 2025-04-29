def search_minor(arr): # function to search the least number in the array
    minor = arr[0] # let's say that it is the first item, to start
    minor_index = 0 # let's say that it is the first item, to start (its index)
    for i in range(1, len(arr)): # now, we iterate over the rest of the array
        if arr[i] < minor: # if the current item is less than the current least...
            minor = arr[i] # then set the least number as the found one
            minor_index = i # then set the least number's index as the found one
    return minor_index # after iterating through the array, return the index of the least number

def selection_sort(arr): # selection sort, a slower way to sort an array
    sorted_arr = [] # the sorted array will be populated
    for i in range(len(arr)): # let's iterate over the entire array that needs to be sorted
        minor_index = search_minor(arr) # let's find its least number using our function created above
        # then, we remove the least number from the array to be sorted
        # and we add it to the sorted array
        sorted_arr.append(arr.pop(minor_index))
    return sorted_arr # after finishing it, the sorted array is returned

print(selection_sort([5, 3, 6, 2, 10])) # => [2, 3, 5, 6, 10]
print(selection_sort([15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])) # => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]