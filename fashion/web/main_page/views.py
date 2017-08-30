from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
import requests
import json
from django.http import JsonResponse

# Create your views here.


def main_page(request):

    return render(request, 'web/main_page/main_page.html')
