from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,'introduction.html')

def hello_world(request):
    return render(request,'hello_world.html')