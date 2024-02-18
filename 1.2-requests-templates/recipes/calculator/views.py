from django.shortcuts import render

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
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
def omlet(request):
    servings = int(request.GET.get("servings", 1))
    context = {
        "recipe": {
            list(DATA.get("omlet").keys())[0]: list(DATA.get("omlet").values())[0] * servings,
            list(DATA.get("omlet").keys())[1]: list(DATA.get("omlet").values())[1] * servings,
            list(DATA.get("omlet").keys())[2]: list(DATA.get("omlet").values())[2] * servings,
        }
    }
    return render(request, 'calculator/index.html', context)
def pasta(request):
    servings = int(request.GET.get("servings", 1))
    context = {
        "recipe": {
            list(DATA.get("pasta").keys())[0]: list(DATA.get("pasta").values())[0] * servings,
            list(DATA.get("pasta").keys())[1]: list(DATA.get("pasta").values())[1] * servings,
        }
    }
    return render(request, 'calculator/index.html', context)
def buter(request):
    servings = int(request.GET.get("servings", 1))
    context = {
        "recipe": {
            list(DATA.get("buter").keys())[0]: list(DATA.get("buter").values())[0] * servings,
            list(DATA.get("buter").keys())[1]: list(DATA.get("buter").values())[1] * servings,
            list(DATA.get("buter").keys())[2]: list(DATA.get("buter").values())[2] * servings,
            list(DATA.get("buter").keys())[3]: list(DATA.get("buter").values())[3] * servings,
        }
    }
    return render(request, 'calculator/index.html', context)