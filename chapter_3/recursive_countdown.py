def recursive_countdown(start): # a simple recursive function to make a countdown
    print(start) # it prints the current number
    if (start <= 1): # the base case: when the countdown reaches 1, stop counting
        return # then, it returns to the previous function call
    else: # otherwise, if there's still a number to count down...
        recursive_countdown(start - 1) # the function is called again with the next number

recursive_countdown(10)