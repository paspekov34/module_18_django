from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class game_shop(TemplateView):
    template_name = 'main_page.html'




class shop_basket(TemplateView):
    template_name = 'basket.html'


def menu_def(request):
    mydict = {'games': ["Atomic Heart", "Cyberpunk 2077"]}
    context = {
        'mydict': mydict,
    }
    return render(request, 'shop.html', context)