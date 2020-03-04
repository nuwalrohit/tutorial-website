from django.shortcuts import render
def index(request):
    return render(request, 'index.html')

def profile(request):
    return render(request,'feedback.html')
def login(request):
    return render(request,'login.html')
def reg(request):
    return render(request,'registration.html')
def page(request):
    return render(request,'1.html')

# Create your views here.
