from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('feedback',views.profile,name='feedback'),
    path('registration',views.reg,name='registration'),
    path('login',views.login,name='login'),
    path('content',views.page,name='1'),
    
]
