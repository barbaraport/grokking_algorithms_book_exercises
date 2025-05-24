def find_biggest_value(items_list):
    if (len(items_list) == 0):
        return 0
    else:
        current = items_list[0]
        _next = find_biggest_value(items_list[1:])

        if _next > current:
            current = _next

        return current

print(find_biggest_value([0, 10]))
print(find_biggest_value([1, 2, 5, 3, 4]))
print(find_biggest_value([]))