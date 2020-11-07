from django.views.generic import ListView
from django.shortcuts import render
from mood.models import Mood, Questions
from django.views.generic.base import TemplateView

class MoodListView(ListView):
    template_name = 'mood_list.html'
    context_object_name = 'mood_list'
    model = Mood

class HomePage(TemplateView):
    template_name = 'home.html'
    
    def get(self, request, *args, **kwargs):
        context = {'question': Questions.objects.first()}
        return render(request, "home.html", context=context)

    def post(self, request, *args, **kwargs):
        return render(request, "home.html")
