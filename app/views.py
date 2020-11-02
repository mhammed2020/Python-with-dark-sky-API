from django.shortcuts import render

# Create your views here.
from darksky import forecast
from datetime import datetime, timedelta
key = 'dd4652c4b7d73db2e67d5ab119689cc4'
def home(request) :
    boston = 42.3601, -71.0589


    return render(request,'home.html',{})