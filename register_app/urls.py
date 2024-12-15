from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/type1/', views.register_type1, name='register_type1'),
    path('register/type2/', views.register_type2, name='register_type2'),
    path('login/', views.custom_login, name='login'),
    path('dashboard/type1/', views.type1_dashboard, name='type1_dashboard'),
    path('dashboard/type2/', views.type2_dashboard, name='type2_dashboard'),
    path('logout/', views.logout_view, name='logout'),
]
