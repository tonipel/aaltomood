from django.views.generic import ListView
from mood.models import Mood
from django.views.generic.base import TemplateView

class MoodListView(ListView):
    template_name = 'mood_list.html'
    context_object_name = 'mood_list'
    model = Mood

class HomePage(TemplateView):
    template_name = 'home.html'
    