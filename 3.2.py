orange_objects = {"basketball", "fanta", "orange", "autumn leaves", "mandarin"}

red_fruits = {"apple', 'crab', 'rose', 'strawberry"}

orange_fruits = {"orange", "mandarin"}

red_orange_fruits = red_fruits.union(orange_fruits)

print("Red and Orange Fruits:", red_orange_fruits)

all_objects = {"basketball", "fanta", "orange", "autumn leaves", 
               "mandarin", 'apple', 'crab', 'rose', 'strawberry'}

objects_without_fruits = all_objects.difference(red_orange_fruits)

print("Objects without Fruits:", objects_without_fruits)