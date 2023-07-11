from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#from .cart import Cart

#def add_to_cart(request, )

def index(request):
    #eturn HttpResponse('Cart')
    return render(request, 'cart/index.html')