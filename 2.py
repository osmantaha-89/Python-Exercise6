def check_and_add_key(my_dict, key):
    if key in my_dict:
        print(f"{key} is in the dictionary!")
    else:
        print(f"{key} is not in the dictionary!")
        my_dict[key] = "empty"
        print(f"The new dictionary is: {my_dict}")

# Example 1
my_dict_1 = {"dad": "Eise", "sister_1": "Iris", "sister_2": "Nicky"}
key_1 = "dad"
check_and_add_key(my_dict_1, key_1)

# Example 2
my_dict_2 = {"fruit": "Apple", "vegetable": "Capsicum"}
key_2 = "meat"
check_and_add_key(my_dict_2, key_2)