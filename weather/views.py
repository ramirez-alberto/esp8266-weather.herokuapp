from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Weather_data
from django.utils import timezone

# Create your views here.
@csrf_exempt
def index(request):
    data = Weather_data(wd_humidity=request.POST['hum'],wd_temp=request.POST['temp'],wd_date = timezone.now())
    data.save()
    context = {'message' : ' '}
    print(context)
    return render(request,'weather/index.html',context)

    
def form(request):
    
    return render(request,'weather/prueba.html')