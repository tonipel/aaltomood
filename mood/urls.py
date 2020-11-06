from django.urls import path

from mood.views import MoodListView

urlpatterns = [
    path('moods', MoodListView.as_view(), name='index'),
]
