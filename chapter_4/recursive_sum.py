def my_sum(numbers):
    if numbers:
        return numbers[0] + my_sum(numbers[1:])
    else:
        return 0

print(my_sum([10, 0]))
print(my_sum([5, 2]))