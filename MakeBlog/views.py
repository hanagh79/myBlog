from django.shortcuts import render
from django.shortcuts import HttpResponse

def about(request):
    # return HttpResponse('hi hana!!!')
    return render(request, 'about.html')
def home(request):
    # return HttpResponse('welcome home')
    return render(request, 'Home.html')
