from django.shortcuts import render

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')

def food(request):
    # date = dt.date.today()
    return render(request, 'all-news/food.html')
def sports(request):
    # date = dt.date.today()
    return render(request, 'all-news/sports.html')
def tech(request):
    # date = dt.date.today()
    return render(request, 'all-news/tech.html')

def travel(request):
    # date = dt.date.today()
    return render(request, 'all-news/travel.html')    
