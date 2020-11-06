from django.views.generic import ListView
from mood.models import Mood

class MoodListView(ListView):
    template_name = 'mood_list.html'
    context_object_name = 'mood_list'
    model = Mood
