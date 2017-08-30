from django.conf import settings
from django.conf.urls import include, url

from web.main_page.views import main_page
from web.evaluation.views import evaluation

app_name = 'web'

urlpatterns = [

	url(r'^$', main_page, name='main_page'),
	url(r'^evaluation/$', evaluation, name='evaluation'),

]
