from django.shortcuts import render, HttpResponse
from pprint import pprint
import random

# Create your views here.
def index(request):
    # print(request)
    # print(type(request))
    # pprint(request.META)
    return HttpResponse('Welcome to Django !')
    
def dinner(request):
    menus = ['장조림버터밥', '왕꼬치구이', '팽이버섯된장국', '단무지무침', '매실차']
    pick = random.choice(menus)
    return render(request, 'dinner.html', {'menus' : menus, 'pick' : pick})