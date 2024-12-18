food=("apple", "banana", "orange", "mango", "strawberry", "grape", "mandarin", "strawberry")
print(food)
print(food[0])
print(food[2])

calories=(52, 96, 62, 605, 33, 68, 50, 33)
print(calories)

foods=list(food)
calories1=list(calories)

print(foods)
print(calories1)

print(foods[4])
print(calories1[4])

print(foods[-2])
print(calories1[-2])

foods_set=set(foods)
print(foods_set)

calories_set=set(calories1)
print(calories_set)

{'apple', 'mandarin', 'orange', 'banana', 'grape', 'mango', 'strawberry'}
{96, 33, 68, 50, 52, 605, 62}

dictionary = dict(zip(food, calories))
print(dictionary)

dictionary["tomato"]=60
print(dictionary)