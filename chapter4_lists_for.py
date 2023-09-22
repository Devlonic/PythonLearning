# 4.1
pizza_list = ['Barbecue', 'Pepperoni', 'Havai']
for pizza in pizza_list:
    print("I like", pizza, "pizza")

print("I really like pizza!")

# 4.2
animals = ['Cat', 'Dog', 'Ants']
for pet in animals:
    print("I think, ", pet, " would be a good pet")

print("I think, that all of this animals is great!")

numbers = range(2, 60, 2)
for num in numbers:
    print(num)

print("min, max, sum",
      min(numbers),
      max(numbers),
      sum(numbers))

squares = [i ** 2 for i in range(2, 10)]
print(squares)

# 4.3
for i in range(1, 21):
    print(i, end=" ")

one_to_million_list = range(1, 1000000)

# 4.4
# for i in one_to_million_list:
#     print(i)

# 4.5
one_to_million_list_second = range(1, 1000001)
if min(one_to_million_list_second) != 1 or max(one_to_million_list_second) != 1000000:
    print("\n4.5 task list is invalid!")

one_to_million_list_second_sum_result = sum(one_to_million_list_second)

print(f"\nSum is {one_to_million_list_second_sum_result}")

# 4.6
for i in range(1, 20, 2):
    print(i, end=" ")

# 4.7
print("")
for i in range(3, 20, 3):
    print(i, end=" ")

# 4.8
print("\ncubes:")
for j in [i**3 for i in range(1, 10)]:
    print(j, end=" ")

# 4.9
cubes = [i**3 for i in range(1, 10)]

# 4.10
take_from = 3
take_to = 5
print(cubes[:take_to])

my_list = ["hello", "nigga", "kaka", 1]
print(my_list)
my_refered_list = my_list
print(my_refered_list)
my_list.remove(1)
print(my_list)
print(my_refered_list)
my_refered_list.insert(1, "adssdsadsda")
print(my_list)
print(my_refered_list)

my_copied_list = my_list[:]
print(my_list)
print(my_refered_list)
print(my_copied_list)

del my_list[0]

print(my_list)
print(my_refered_list)
print(my_copied_list)

# 4.11
friend_pizzas = pizza_list[:]

new_pizza_old_list = "new pizza at old list"
new_pizza_new_list = "new pizza at new list"

pizza_list.insert(0, new_pizza_old_list)
friend_pizzas.insert(0, new_pizza_new_list)

print(f"Old list: {pizza_list}\nNew list: {friend_pizzas}")

# 4.12
for square in squares:
    print(square, end=" ")

# 4.13
dishes = ("potato", "fish", "orange", "kaka", "mayo")

print()
for dish in dishes:
    print(dish, end=" ")

try:
    dishes[2] = ""
except:
    print("\nerror!")

dishes = ("new_dish1", "new_dish2",
          dishes[0], dishes[1], dishes[2], dishes[3], dishes[4])
for dish in dishes:
    print(dish, end=" ")

# 4.15 show vertical line vs code on 80 and 100 col: "editor.rulers": [80, 100]
# show
# ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd

my_list_second = []

for num in range(1, 11):
    my_list_second.append(num)

print(my_list_second)
