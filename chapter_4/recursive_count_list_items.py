def count_items(items_list):
    if (len(items_list) == 0):
        return 0
    else:
        return 1 + count_items(items_list[1:])
    
print(count_items([0]))
print(count_items([0, 0, 0, 0]))
print(count_items([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]))