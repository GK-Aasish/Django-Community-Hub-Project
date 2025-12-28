from django.urls import path
from .views.main_view import index
from .views.auth_view import signup_view, login_view
from .views.components_view import user_settings


urlpatterns = [
    path('', index, name='dashboard'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('user-settings/', user_settings, name='user_settings'),
]
