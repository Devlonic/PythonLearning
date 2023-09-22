# #  7.1
# car = input("какую машину он хотел бы взять напрокат?: ")
# print(f"Let me see if I can find you a {car}")

# # 7.2
# count = int(input("на сколько мест you хочет забронировать стол в ресторане?: "))
# if count > 8:
#     print('You should wait')
# else:
#     print('Your table is ready')

# # 7.3
# print((int(input("Enter number: ")) % 10) == 0)

# # 7.4
# toppings = []
# while True:
#     desired_topping = input("Enter topping: ")
#     if desired_topping == 'quit':
#         break
#     else:
#         toppings.append(desired_topping)
#         print(f'Topping {desired_topping} was included to your order')

# print("Your toppings is: ", toppings)

# # 7.5

# while True:
#     age = input("Enter age('q' - to stop progrm): ")
#     if age == 'q':
#         break
#     else:
#         age = int(age)
#         if age < 3:
#             print("*free*")
#         elif age >= 3 and age < 12:
#             print('10$')
#         else:
#             print("15$")

# # 7.6

# toppings = []
# desired_topping = ''
# active = True
# i = 5
# while desired_topping != 'q' and active:
#     desired_topping = input("Enter topping: ")
#     if desired_topping == 'quit':
#         break
#     elif desired_topping != 'q':
#         toppings.append(desired_topping)
#         print(f'Topping {desired_topping} was included to your order')
#     i -= 1
#     if i == 0:
#         active = False
# print("Your toppings is: ", toppings)

# # 7.7
# while (2 + 2) != 5:
#     print("The math is fine")

# 7.8
sandwich_orders = [
    'Sandw1',
    'Sandw2',
    'Sandw3',
    'Sandw4',
]

finished_sandwiches = []

print(sandwich_orders)
print(finished_sandwiches)


while len(sandwich_orders) > 0:
    buf = sandwich_orders.pop()
    finished_sandwiches.append(buf)
    print(f"I made you {buf} sandwich")

print(sandwich_orders)
print(finished_sandwiches)

# 7.9

sandwich_orders = [
    'Sandw1',
    'pastrami',
    'Sandw2',
    'pastrami',
    'Sandw3',
    'Sandw4',
    'pastrami'
]

finished_sandwiches = []

print(sandwich_orders)
print(finished_sandwiches)
print("Pastrami cannot be ordered")

while len(sandwich_orders) > 0:
    buf = sandwich_orders.pop()
    if (buf == 'pastrami'):
        print("Sorry, but pastrami cannot be ordered")
        continue
    finished_sandwiches.append(buf)
    print(f"I made your {buf} sandwich")

print(sandwich_orders)
print(finished_sandwiches)

# 7.10
users = ["Ivan", "Kaban", "Debilos", "Jopas Negras"]
results = []

buf = ''
for user in users:
    buf = input(f"Hello, {user}, where you want to go at the weekend?: ")
    results.append((user, buf))

print(results)
