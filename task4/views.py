from django.shortcuts import render


def main_page(request):
    return render(request, 'fourth_task/menu.html')


def store_page(request):
    fruits = {'fruits': ['Apple', 'Pineapple', 'Orange']}
    return render(request, 'fourth_task/store.html', context=fruits)


def cart_page(request):
    return render(request, 'fourth_task/cart.html')
