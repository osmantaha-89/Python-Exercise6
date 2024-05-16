def check_dict_empty(dictionary):
    if not dictionary:  
        print("This dictionary is empty")
    else:
        print("This dictionary is not empty")

# Example 1
my_dict1 = {0: 19, 1: 33, 2: 18, 3: 30, 4: 26}
check_dict_empty(my_dict1)

# Example 2
my_dict2 = {}
check_dict_empty(my_dict2)