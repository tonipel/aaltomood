from django.urls import path

from mood.views import MoodListView
from mood.views import HomePage

urlpatterns = [
    path('moods', MoodListView.as_view(), name='index'),
    path('home', HomePage.as_view(), name='home')
]
