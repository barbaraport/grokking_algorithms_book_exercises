def quicksort(array):
    if len(array) < 2: # array with none or one item
        return array # if the array is empty or has one item, it is already sorted
    else:
        pivot = array[0] # let's say that our pivot is the first item. but it works with any index
        least_items = [i for i in array[1:] if i <= pivot] # gets all items least than or equal the pivot (disconsider the pivot - "1:")
        greater_items = [i for i in array[1:] if i > pivot] # gets all items greater than the pivot (disconsider the pivot - "1:")
        return quicksort(least_items) + [pivot] + quicksort(greater_items) # sorts the least and greater items, until reaching the base case.

print(quicksort([10, 5, 2, 3]))
print(quicksort([-1, 0, 3, 2, 6, 7, -22]))
print(quicksort([]))
print(quicksort([1]))
print(quicksort([1, 1]))