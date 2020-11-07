import datetime
from django.views.generic import ListView
from django.shortcuts import render
from mood.models import Mood, Questions, Person
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class MoodListView(ListView):
    template_name = 'mood_list.html'
    context_object_name = 'mood_list'
    model = Mood

class HomePage(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'
    
    def get(self, request, *args, **kwargs):
        context = {'question': Questions.objects.first()}
        return render(request, "home.html", context=context)

    def post(self, request, *args, **kwargs):
        for i in range(6):
            if str(i) in request.POST:
                create_mood(str(i), request.user)
                break
        return render(request, "home.html")

def create_mood(button_name_id, user):
    pass
    # person = Person.objects.get_or_create(user=user)[0]
    # mood = Mood.objects.create(user=person,
    #                            date=datetime.datetime.utcnow(),
    #                            value=button_name_id)
