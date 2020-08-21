from django.urls import path
from .views import*
from .views_user import*
urlpatterns = [
    path('', index, name='home'),
]