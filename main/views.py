from datetime import date
from django.shortcuts import render

def index(request):
    today = date.today()
    target_date = date(today.year, 6, 6)
    days_left = (target_date - today).days
    return render(request, 'main/index.html', {'days_left': days_left})
from django.shortcuts import render

# Create your views here.
