from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name='python_tutorial'),
    path('hello_world/',views.hello_world,name='hello_world')
]
