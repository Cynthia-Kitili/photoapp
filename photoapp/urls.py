from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^$food/',views.food,name='food'),
    url(r'^$sports/',views.sports,name='sports'),
    url(r'^$tech/',views.tech,name='tech'),
    url(r'^$travel/',views.travel,name='travel'),
]