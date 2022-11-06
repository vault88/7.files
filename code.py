def make_cookbook(file):
    with open(file, 'rt', encoding='utf-8') as f:
        cook_book = {}
        for line in f:
            dish_name = line.strip('\n')
            ingredients_count = int(f.readline())
            # print(ingredients_count)
            ingredients = []
            for _ in range(ingredients_count):
                ingr = f.readline().split(' | ')
                ingredient_name, quantity, measure = ingr
                ingredients.append({'ingredient_name': ingredient_name.strip('\n'), 'quantity': quantity.strip('\n'), 'measure': measure.strip('\n')})
            f.readline()
            cook_book[dish_name] = ingredients
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    ingredient_list = []
    for dish in dishes:
        ingredient = make_cookbook('recipes.txt').get(dish)
        ingredient_list += ingredient
    my_dict = {}
    for element in ingredient_list:
        name = element.get('ingredient_name')
        quantity = int(element.get('quantity'))
        measure = element.get('measure')
        if name in my_dict:
            number = int(my_dict.get(name).get('quantity')) + quantity
            my_dict[name] = {'measure': measure, 'quantity': number * int(person_count)}
        else:
            my_dict[name] = {'measure': measure, 'quantity': quantity * int(person_count)}
    print(my_dict)

# make_cookbook('recipes.txt')
get_shop_list_by_dishes(['Запеченный картофель','Омлет'], 2)