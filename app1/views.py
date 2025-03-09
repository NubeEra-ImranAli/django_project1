
from django.shortcuts import render

def home(request):
    return render(request, 'app1/index.html')
def index2(request):
    return render(request, 'app1/index2.html')