from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    data = None
    # a = request.get('https://restcountries.com/v2/all')
    # data = a.json()
    if request.method == "POST":
        country = request.POST.get('search')
        print(country)
        a = requests.get(f'https://restcountries.com/v2/name/{country}')
        data = a.json()
        print(data)
    return render(request,'index.html',{'data':data})
