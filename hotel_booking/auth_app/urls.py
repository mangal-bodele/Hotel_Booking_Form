from django.urls import path
from .views import login_hotel,logout_hotel,change_pass,signup_hotel
urlpatterns = [
    path('signup/',signup_hotel,name='signup_url'),
    path('login/',login_hotel,name='login_url'),
    path('logout/',logout_hotel,name='logout_url'),
    path('change_pass/',change_pass,name='change_url')
]