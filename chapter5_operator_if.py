# 5.1
car = "subaru"
my_num = 2
concated_car = "su" + "baru"
my_positive_boolean_value = True == True
my_string_num = "2"

print("Is car == 'subaru'? I predict True", car == "subaru")
print("Is car == concated_car? I predict True", car == concated_car)
print("Is my_num == 2? I predict True", my_num == 2)
print("Is my_num != '2'? I predict True", my_num != "2")
print("Is bool(my_string_num) == my_positive_boolean_value? I predict True",
      bool(my_string_num) == my_positive_boolean_value)

print("Is car == 'SuBaRu'? I predict False", car == "SuBaRu")
print("Is my_num == my_string_num? I predict False", my_num == my_string_num)
print("Is len(car) == 7? I predict False", len(car) == 7)
print("Is 2**3 == 6? I predict False", 2**3 == 6)
print("Is True == False? I predict False", True == False)

# 5.2
print("kaka" == 'ka'+'ka')
print("kaka" == "KakA")
print("kaka" == str.lower("KakA"))
print("kaka" == str.lower("KakAa"))
print(5 == 5)
print(4 == 5)
print(5 != 5)
print(4 != 5)
print(4 < 5)
print(5 > 5)
print(5 >= 5)
print(4 >= 5)
print(5 <= 5)
print(6 <= 5)
print(6 == 6 and 5 <= 5)
print(6 == 6 and 5 < 5)
print(6 != 6 or 5 == 5)
print(6 != 6 or 5 > 5)
print('ivan' in ['ivan', 'max', 'kaka', 'vasya'])
print('ivaNNnn' in ['ivan', 'max', 'kaka', 'vasya'])
print('ivaNNnn' not in ['ivan', 'max', 'kaka', 'vasya'])
print('ivan' not in ['ivan', 'max', 'kaka', 'vasya'])

# 5.3

# 5.3.1
alien_color = 'green'
if alien_color == 'green':
    print('You earn 5 points!')

# 5.3.2
alien_color = 'red'
if alien_color == 'green':
    print('You earn 5 points!')

# 5.4

# 5.4.1
alien_color = 'green'
if alien_color == 'green':
    print('You earn 5 points!')
else:
    print('You earn 10 points!')

# 5.4.2
alien_color = 'red'
if alien_color == 'green':
    print('You earn 5 points!')
else:
    print('You earn 10 points!')

# 5.5

# 5.5.1
alien_color = 'green'
if alien_color == 'green':
    print('You earn 5 points!')
elif alien_color == 'yellow':
    print('You earn 10 points!')
elif alien_color == 'red':
    print('You earn 15 points!')

# 5.5.2
alien_color = 'yellow'
if alien_color == 'green':
    print('You earn 5 points!')
elif alien_color == 'yellow':
    print('You earn 10 points!')
elif alien_color == 'red':
    print('You earn 15 points!')

# 5.5.3
alien_color = 'red'
if alien_color == 'green':
    print('You earn 5 points!')
elif alien_color == 'yellow':
    print('You earn 10 points!')
elif alien_color == 'red':
    print('You earn 15 points!')

# 5.6
human_age = 20
period = 'none'

if human_age < 2:
    period = 'newborn'
elif 2 <= human_age < 4:
    period = 'toddler'
elif 4 <= human_age < 13:
    period = 'child'
elif 13 <= human_age < 20:
    period = 'teen'
elif 20 <= human_age < 65:
    period = 'adult'
elif 60 <= human_age:
    period = 'elderly'
print(period)

# 5.7
my_fav_fruits = ['apple', 'pineapple', 'banana']
fruits = ['kaka', 'peach', 'mango', 'apple', 'pineapple', 'banana']

for f in fruits:
    if f in my_fav_fruits:
        print(f'You really like {f}!')

# 5.8
user_list = ['ivan', 'johnny', 'jac', 'admin', 'akkakiy']
admin_list = ['admin', 'jac']

for user in user_list:
    if user in admin_list:
        print(f"Welcome, admin {user}! Would you like to open admin panel?")
    else:
        print(f"Welcome, {user}!")

# 5.9
user_list.clear()
if len(user_list) == 0:
    print("We need to find some users!")

# 5.10
current_users = ['Ivan', 'johnny', 'jac', 'admin', 'akkakiy']
new_users = ['kaka', 'dasasd', 'jac', 'admin', 'new_user', 'IvAn']

for new_user in new_users:
    if (new_user.lower() in [u.lower() for u in current_users]):
        print(f'User {new_user} already exist. Change name')

# 5.11
numbers = range(1, 10)
for num in numbers:
    if num == 1:
        print(f'{num}st')
    elif num == 2:
        print(f'{num}nd')
    elif num == 3:
        print(f'{num}rd')
    else:
        print(f'{num}th')

# 5.12
# everything is fine

# 5.13
# хочу написати на c# бекенд для telegram-бота,
# якого напишуть на пайтоні.
# крім того, хочу написати якийсь bruteforce-застосунок,
# оскільки python дуже добре для цього підходить.
