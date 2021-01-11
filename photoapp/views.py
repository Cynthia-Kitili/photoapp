from django.shortcuts import render

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')

def category(request):
    images = Image.objects.all()
    return render(request, 'category.html',{'images':images})