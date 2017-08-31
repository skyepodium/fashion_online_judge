from django.conf import settings
from django.conf.urls import include, url

from web.main_page.views import main_page
from web.evaluation.views import evaluation
from django.http import HttpResponse

app_name = 'web'

def heart_beat(request):
    return HttpResponse("It's Works!", content_type='text/plain')

urlpatterns = [

	url(r'^$', main_page, name='main_page'),
	url(r'^evaluation/$', evaluation, name='evaluation'),
	url('^heart_beat/', heart_beat),

]
