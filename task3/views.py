from django.shortcuts import render


def main_page(request):
    return render(request, 'third_task/main.html')


def store_page(request):
    fruits = {
        'first': 'Apple',
        'second': 'Pineapple',
        'third': 'Orange'
    }
    return render(request, 'third_task/store.html', context=fruits)


def cart_page(request):
    return render(request, 'third_task/cart.html')
