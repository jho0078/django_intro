from django.shortcuts import render
from datetime import datetime
import requests
import os



# Create your views here.
def index(request):
    return render(request, 'utilities/index.html')
    
def bye(request):
    datetimenow = datetime.now()
    datebye = datetime(2019, 2, 28)
    dday = datebye - datetimenow
    return render(request, 'utilities/bye.html', {'dday' : dday})
    
def graduation(request):
    datetimenow = datetime.now()
    datebye = datetime(2019, 5, 28)
    dday = (datebye - datetimenow).days
    return render(request, 'utilities/graduation.html', {'dday' : dday})
    
def imagepick(request):
    return render(request, 'utilities/imagepick.html')
    
def today(request):
    key = os.getenv("WEATHER")
    url = f'https://api.openweathermap.org/data/2.5/weather?q=Daejeon,kr&lang=kr&APPID={key}'
    req = requests.get(url).json()
    sky = req['weather'][0]['description']
    tem = req['main']['temp']
    tem_min = req['main']['temp_min']
    tem_max = req['main']['temp_max']
    
    return render(request, 'utilities/today.html', 
                {'sky': sky, 'tem': tem, 'tem_min': tem_min, 'tem_max': tem_max})
                
def ascii_new(request):
    return render(request, 'utilities/ascii_new.html')
    
def ascii_make(request):
    text = request.GET.get('text')
    font = request.GET.get('fonts')
    url = f'http://artii.herokuapp.com/make?text={text}&font={font}'
    req = requests.get(url).text
    return render(request, 'utilities/ascii_make.html', {'req': req})
    
def original(request):
    return render(request, 'utilities/original.html')
    
def translated(request):
    content = request.GET.get('content')
    
    naver_client_id = os.getenv("NAVER_CLIENT_ID")
    naver_client_secret = os.getenv("NAVER_CLIENT_SECRET")
    
    papago_url = "https://openapi.naver.com/v1/papago/n2mt"
    
    headers = {
    "X-Naver-Client-Id": naver_client_id,
    "X-Naver-Client-Secret": naver_client_secret
    }
    data = {
    "source": "ko",
    "target": "en",
    "text": content
    }
    papago_response = requests.post(papago_url, headers=headers, data=data).json()
    
    reply_text = papago_response["message"]["result"]["translatedText"]
    
    
    return render(request, 'utilities/translated.html', {'reply_text': reply_text})