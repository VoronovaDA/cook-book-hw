import pprint

with open('data.txt', encoding = 'utf-8') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        ing_count = int(file.readline())
        ingredients = []
        for ing in range(ing_count):
            ingredient = file.readline().strip()
            ingredient_name, quantity, measure = ingredient.split(' | ')
            ingredients.append({
                'ingredient_name' : ingredient_name,
                'quantity' : quantity,
                'measure' : measure
            })
        file.readline()
        cook_book[dish_name] = ingredients
            
pprint.pprint(cook_book)

print()

def get_shop_list_by_dishes(dishes, person_count):
    ing_list = {}
    with open('data.txt', encoding='utf-8') as file:
        cook_book = {}
        for line in file:
            dish_name = line.strip()
            ing_count = int(file.readline())
            ingredients = []
            for ing in range(ing_count):
                ingredient = file.readline().strip()
                ingredient_name, quantity, measure = ingredient.split(' | ')
                ingredients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': quantity,
                    'measure': measure
                })
            file.readline()
            cook_book[dish_name] =  ingredients

    for dish in dishes:
        for shopping_pos in cook_book[dish]:
            ing_name, amount, string = shopping_pos.values()
            if ing_name in ing_list.keys():
                ing_list[ing_name]['quantity'] += int(amount) * person_count
            else:
                ing_list[ing_name] = {'measure': string, 'quantity': int(amount) * person_count}
    return ing_list

pprint.pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))