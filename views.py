from django.http import HttpResponse
from django.shortcuts import render

import urllib3
import requests


# Create your models here.

def getjsondata(request):
    url = 'https://api.citybik.es/v2/networks/bikerio'
    myobj = {'somekey': 'somevalue'}

    x = requests.get(url, json=myobj)

    return HttpResponse(x.content)

