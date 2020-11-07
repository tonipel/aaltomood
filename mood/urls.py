from django.urls import path
from mood.views import HomePage

urlpatterns = [
    path('home', HomePage.as_view(), name='home')
]
