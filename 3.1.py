red_objects = {'apple', 'crab', 'rose', 'strawberry'}

fruits = {'orange', 'apple', 'strawberry', 'grape', 'kiwi', 'mandarin'}

red_fruits = red_objects.intersection(fruits)

non_red_fruits = fruits.difference(red_fruits)

print("Red fruits: ", red_fruits)
print("Non-red fruits: ", non_red_fruits)