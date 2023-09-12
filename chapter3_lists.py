# 3.1
friend_names = ["ivan", "petro", "akakiy", "afanasiy", "john sena"]

print(friend_names[0])
print(friend_names[1])
print(friend_names[2])
print(friend_names[-2])
print(friend_names[-1])

# 3.2
message = ": hello, my friend!"
print(friend_names[0], message)
print(friend_names[1], message)
print(friend_names[2], message)
print(friend_names[3], message)

# 3.3
motocycles = ['honda', 'dugatti', 'bmw']
print("I would like to buy", motocycles[0], sep='\t')
print("I would like to buy", motocycles[-1], sep='\t')

# 3.4
people = ['ivan', 'karas', 'taras', 'piter']
print('Come to me, ', people[0], ", to dinner")
print('Come to me, ', people[1], ", to dinner")
print('Come to me, ', people[2], ", to dinner")
print('Come to me, ', people[3], ", to dinner")

# 3.5
print("\n\n")
missing_guest = 1
print(f'{people[missing_guest]} cannot come.')
del people[missing_guest]
people.insert(missing_guest, "akakiy")
print('Come to me, ', people[0], ", to dinner")
print('Come to me, ', people[1], ", to dinner")
print('Come to me, ', people[2], ", to dinner")
print('Come to me, ', people[3], ", to dinner")

# 3.6
people.insert(0, "firstGuestTest")
people.append("lastGuestTest")
people.insert(int(len(people)/2), "middleGuestTest")
print(people)

print("only 2 people can be invitated")
print("im sorry, but get out of my table, ", people.pop())
print("im sorry, but get out of my table, ", people.pop())
print("im sorry, but get out of my table, ", people.pop())
print("im sorry, but get out of my table, ", people.pop())
print("im sorry, but get out of my table, ", people.pop())
print(people)
print('Come to me, ', people[0], ", to dinner")
print('Come to me, ', people[1], ", to dinner")
del people[0]
del people[0]
print(len(people) == 0)

# 3.8
countries = ['North Korea', "Taliban", "Iran", "Syria", "Algeria"]
print(countries)
print(sorted(countries))
print(countries)
countries.reverse()
print(countries)
countries.reverse()
print(countries)
countries.sort()
print(countries)
countries.sort(reverse=True)
print(countries)

# 3.9
print("count of countries: ", len(countries))

# 3.10
languages = ["UA", "EN", "PL", "AR", "IN"]
languages.append('KAKA')
del languages[0]
print(languages)
languages.reverse()
print(sorted(languages))
print(languages)
languages.sort()
languages.insert(2, "adsasd")
print(len(languages))

# just for example
print(pow(2, 4) == 2**4)

# 3.11
print(languages)
# del languages[1000]
# del languages[-1000]

my_list = ['ads', 'dsadasads', '3223232sad']
print(my_list.pop())
print(my_list)
del my_list[0]
print(my_list)
