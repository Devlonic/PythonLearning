# 6.1
human_params = {
    'first_name': "Ivan",
    'last_name': "Akakiev",
    'age': 52,
    'city': 'Lutsk',
}

print(f"""
***Info about {human_params['last_name']}***
Name: {human_params['first_name']} 
Surname: {human_params['last_name']} 
Age: {human_params['age']} 
Location: {human_params['city']} 
***
""")

# 6.2
fav_numbers = {
    'Ivan': 4,
    'Max': 13,
    'Adolf': 1488,
    'Tesak': 1488,
    'Vasek': 228,
    'Lucik': 666,
    'Ivacik': 666,

}

for name in fav_numbers:
    print(f"Favourite {name}`s number is {fav_numbers[name]}")

# 6.3
glossary = {
    'Interpolation': 'Процесс вставки в текст якихось данних',
    'List': 'Коллекція, здатна зберігати дані у вигляді матриці-рядка',
    'Tuple': 'Незміна колекція, елементи якої не можна змінити в runtime',
    'Condition': """Дослівно перекладається як 'Умова'. 
    Повертає True або False в залежності від істинності 
    чи хибності логічного виразу""",
    'Operand': 'Змінна, над якою відбувається якась певна дія',
}

# for term in glossary:
#     print(f"\nWord {term} mean: {glossary[term]}")

# 6.4

for term, meaning in glossary.items():
    print(f"\nWord {term} mean: {meaning}")

# 6.5
rivers_countries = {
    'dnipro': 'ukraine',
    'nile': 'egypt',
    'styr': 'ukraine',
    'missisipy': 'usa',
}
for river, country in rivers_countries.items():
    print(f"The {river.title()} runs through {country.title()}")
for river in rivers_countries.keys():
    print(f"{river.title()}")
for country in rivers_countries.values():
    print(f"{country.title()}")

# 6.6
people = ['jeb', 'jen', 'max', 'edward', 'phil', 'ivan', 'sarah']

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for person in people:
    if person in favorite_languages.keys():
        print(f"Thanks you, {person}, for membering in our quitz")
    else:
        print(f"Would you like to start quitz, {person}?")

# 6.7

human_params = {
    'first_name': "Ivan",
    'last_name': "Akakiev",
    'age': 52,
    'city': 'Lutsk',
}

people_list = [
    human_params,
    {
        'first_name': "Jopas",
        'last_name': "Negretos",
        'age': 66,
        'city': 'Rio',
    },
    {
        'first_name': "Max",
        'last_name': "Oersqwe",
        'age': 20,
        'city': 'Lutsk',
    }
]

for person in people_list:
    print(f"""
***Info about {person['last_name']}***
Name: {person['first_name']} 
Surname: {person['last_name']} 
Age: {person['age']} 
Location: {person['city']} 
***
""")

# 6.8
pets = [
    {'name': 'vasek', 'params': {'type': 'cat', 'owner': 'kaka'}},
    {'name': 'kulik', 'params': {'type': 'dog', 'owner': 'jacob'}},
    {'name': 'dima', 'params': {'type': 'human', 'owner': 'masha'}},
]

for pet in pets:
    print(f"""
***Info about {pet['name']}***
Name: {pet['name']}  
Type: {pet['params']['type']} 
Owner: {pet['params']['owner']} 
***
""")

# 6.9

fav_places = {
    'Lutsk': ['Ivan', 'Kaban', 'Ibrahim'],
    'LNTU': ['Jacab', 'Ivan', 'Kaban'],
    'Moon': ['Neil', 'Ibrahim', 'Kaban']
}

# take all people names from collection
peoples = [names for names in fav_places.values()]
new_peoples = []
for i in range(0, len(peoples)):
    for person in peoples[i]:
        new_peoples.append(person)
peoples = set(new_peoples)
print(peoples)

for person in peoples:
    print(f"\n{person}: ", end='')
    for place, loved_by in fav_places.items():
        if (person in loved_by):
            print(place, end=' ')

# 6.10

fav_numbers = {
    'Ivan': [4, 5, 66],
    'Max': [13, 123, 333],
    'Adolf': [1488, 1337],
    'Tesak': [1488, 228],
    'Vasek': [228, 44444],
    'Lucik': [666, 5234],
}
print(fav_numbers)

# 6.11
cities = {
    'lutsk': {
        'country': 'Ukraine',
        'population': 120000,
        'fact': 'The best city in the world'
    },
    'rivne': {
        'country': 'Ukraine',
        'population': 140000,
        'fact': 'Post-soviet city'
    },
    'viinutsia': {
        'country': 'Ukraine',
        'population': 250,
        'fact': 'The best village in the world'
    },
}

print(cities)

# 6.12

for person, numbers in fav_numbers.items():
    print(f"{person} likes the numbers: {numbers}")
