def fat(x):
    if x == 1:
        return 1
    else:
        return x * fat(x - 1)
    
print("3! -> " + str(fat(3)))
print("5! -> " + str(fat(5)))
print("10! -> " + str(fat(10)))