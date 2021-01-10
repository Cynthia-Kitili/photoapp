from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^$',views.food,name='food'),
    url(r'^$',views.sports,name='sports'),
    url(r'^$',views.tech,name='tech'),
    url(r'^$',views.travel,name='travel'),
]