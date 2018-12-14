from django.urls import path
from . import views

app_name = 'booking_system'
urlpatterns = [
    path('',views.entrance, name='entrance'),
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout')
]