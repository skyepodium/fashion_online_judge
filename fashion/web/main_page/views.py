from django.shortcuts import render

# Create your views here.


def main_page(request):

    return render(request, 'web/main_page/main_page.html')
