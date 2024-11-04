#app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('handleform', views.handle_form, name='form'),
    #path('', views.index, name='index'),
    path('', views.index_html, name='index'),
    path("dummypage/", views.dummypage, name="index"),
    path('sum/', views.sum_view),
    path('time/', views.time_view),
    path('new/', views.new),
    path('createUser/', views.createUser),
    path('index.html', views.index_html)
]


