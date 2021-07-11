
from django.urls import path
from .import views

app_name='customer'

urlpatterns = [
    path('',views.home,name='home'),
    path('customer/',views.customer_list,name='customer_list'),
    path('history/',views.history,name='history'),
    path('profile/<int:cust_id>',views.profile,name='profile'),
]