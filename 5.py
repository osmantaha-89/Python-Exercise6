def sort_dict_values(my_dict):
    
    sorted_values = sorted(my_dict.values())
   
    sorted_dict = {k: v for k, v in zip(my_dict.keys(), sorted_values)}
    return sorted_dict

my_dict1 = {0: 19, 1: 33, 2: 18, 3: 30, 4: 26}
sorted_dict1 = sort_dict_values(my_dict1)
print('The sorted dictionary is:', sorted_dict1)

my_dict2 = {0: 45, 1: 7, 2: 44, 3: 81, 4: 6}
sorted_dict2 = sort_dict_values(my_dict2)
print('The sorted dictionary is:', sorted_dict2)