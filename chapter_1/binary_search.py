def binary_search(complete_list, item_to_find): # the complete_list needs to be sorted, okay? :)
    # types of index guesses: low or high guesses
    low = 0 # the lower index guess is zero
    high = len(complete_list) - 1 # the higher index guess is the last index of the list

    while low <= high: # while I still have guesses to make
        middle = (low + high) // 2 # middle index of the complete list
        guess = complete_list[middle] # I get the middle item from the complete list, to check it in the ifs below
        
        if guess == item_to_find: # If true, I found the item!!!
            return middle # so I return its index
        if guess > item_to_find: # if the guess item is higher than the item to find, then my guess was too high
            high = middle - 1 # my new value of the high is the middle index minus one item, because I have checked it in this iteration
        else: # if my guess was too low, then I need to increase the middle index because the item to find is greater than the actual value
            low = middle + 1 # adding 1 in the middle index because I have to check the higher values
    
    return None # the item to find was not found :(

my_list = [1, 3, 5, 7, 9] # a test list

print(binary_search(my_list, 3)) # => index 1 (second item in the list)
print(binary_search(my_list, -1)) # => None (it was not found in the list)
print(binary_search([1, 7, 8, 9, 11, 17], 11)) # => index 4
