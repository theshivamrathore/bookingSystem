from django.urls import path
from .views import homeView,loginView,registration,logoutView,buyerDashboard,sellerDashboard

urlpatterns = [
    path('',homeView,name='home-page'),
    path('registration',registration,name='registration'),
    path('login',loginView,name='login'),
    path('logout',logoutView,name='logout'),
    path('buyer-dashboard',buyerDashboard,name='buyer-dashboard'),
    path('seller-dashboard',sellerDashboard,name='seller-dashboard'),
]
