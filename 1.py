def merge_lists_into_dict(list_1, list_2):
    return dict(zip(list_1, list_2))

# Example 1
list_1 = [1, 2, 3, 4]
list_2 = [7, 8, 9, 10]
resulting_dict = merge_lists_into_dict(list_1, list_2)
print("The dictionary is:", resulting_dict)

# Example 2
list_1 = ["one", "two", "three", "four"]
list_2 = [1, 2, 3, 4]
resulting_dict = merge_lists_into_dict(list_1, list_2)
print("The dictionary is:", resulting_dict)