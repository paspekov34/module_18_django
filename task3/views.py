from django.shortcuts import render


# Create your views here.
def main_page_def(request):
    title_mp = 'Главная страница'
    name = 'Главная'
    shop = 'Магазин'
    basket = 'Корзина'
    context = {'title_mp': title_mp, 'name': name,
               'shop': shop, 'basket': basket}
    return render(request, 'Main page.html', context)



def shop_def(request):
    title_shop = 'Вы в магазине'
    game_1 = 'Wither 3'
    game_2 = 'GTA 5'
    game_3 = 'Mortal Kombat'
    context = {'title_mp': title_shop,
               'game_1': game_1,
               'game_2': game_2,
               'game_3': game_3}
    return render(request, 'shop.html', context)


def basket_def(request):
    title_basket = 'Это ваша корзина'
    context = {'title_mp': title_basket}
    return render(request, 'basket.html', context)