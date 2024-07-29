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
    foods = []
    for food in spicy_foods:
        foods.append(food["name"])
    return foods
    
# print(get_names(spicy_foods))


def get_spiciest_foods(spicy_foods):
    spicy = []
    for food in spicy_foods:
        if food["heat_level"] > 5:
            spicy.append(food)
    return spicy


def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

    

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food['heat_level'] > 5:
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")
    
# print_spiciest_foods(get_spicy_food_by_cuisine, spicy_foods, "Sichuan")


def get_average_heat_level(spicy_foods):
    total_heat=0
    for food in spicy_foods:
        total_heat +=food["heat_level"]
    return total_heat/len(spicy_foods)

# print(get_average_heat_level(spicy_foods))

def create_spicy_food(spicy_foods, spicy_food):
    # name=input("Name of food >>>")
    # cuisine=input("Name of cuisine >>>")
    # spice=int(input("spice level >>>"))

    # spicy_food={
    #     "name":name,
    #     "cuisine":cuisine,
    #     "heat_level":spice
    # }
    spicy_foods.append(spicy_food)
    return spicy_foods

# create_spicy_food(spicy_foods)

# print(spicy_foods)

