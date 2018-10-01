from django.conf.urls import url
from scoreBoard import views
from django.urls import path

urlpatterns=[
    path('', views.scores, name='scoreBoard'),
]
