from django.urls import path
from . import views
app_name = 'accounts'
urlpatterns = [
    path('', views.accounts, name = 'accounts'),
    path('signup', views.signup_view, name = 'signup'),
]