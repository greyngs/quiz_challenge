import django
from django.urls import path
from .views import register, home
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('register/', register, name='register_process'),
    path('', home, name='home_process'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login_process'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout_process'),
]
