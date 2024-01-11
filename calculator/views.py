from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },

}


def get_recipe(request, dish: str):
    servings = int(request.GET.get("servings", 1))
    dish_recipe = DATA.get(dish)
    if servings:
        dish_recipe = dish_recipe.copy()
        for item in dish_recipe:
            dish_recipe[item] = dish_recipe[item] * servings
    data = {
        'recipe': dish_recipe
    }
    return render(request, 'calculator/index.html', context=data)
