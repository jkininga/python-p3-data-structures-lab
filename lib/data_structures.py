spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food['name'] for food in spicy_foods ]

# print(get_names(spicy_foods))

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food['heat_level'] > 5 ]

# print(get_spiciest_foods(spicy_foods))

def print_spicy_foods(spicy_foods):
    for i in spicy_foods:
        print(f"{i['name']} ({i['cuisine']}) | Heat Level: {i['heat_level']* '🌶'}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if  food['cuisine'] == cuisine:
            return food


# print(get_spicy_food_by_cuisine(spicy_foods, 'American'))

def print_spiciest_foods(spicy_foods):
    for i in spicy_foods:
        if i['heat_level'] > 5:
            print(f"{i['name']} ({i['cuisine']}) | Heat Level: {i['heat_level']* '🌶'}")
    

# print_spiciest_foods(spicy_foods)

def get_average_heat_level(spicy_foods):
    if not spicy_foods:
        return None
    sumation = 0
    list_of_spices = [food['heat_level'] for food in spicy_foods]

    for i in list_of_spices:
        sumation +=i
    return int(sumation/len(list_of_spices))
    

# print(get_average_heat_level(spicy_foods))

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods


# print(create_spicy_food(spicy_foods, {
#         'name': 'Griot',
#         'cuisine': 'Haitian',
#         'heat_level': 10,
#     } ))
