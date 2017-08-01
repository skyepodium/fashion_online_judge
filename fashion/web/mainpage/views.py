from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def main_page(request):

    return render(request, 'web/main_page/main_page.html')
#    return HttpResponse(1)
