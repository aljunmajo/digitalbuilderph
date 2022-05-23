from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse
from .models import GeneralSettings
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.
class SiteSettings(LoginRequiredMixin, ListView):
    model = GeneralSettings
    template_name = 'site-settings.html'
    #ordering = 'title'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = 'Site title'
        context['testing'] = 'Site testing'
        context['has_permission'] = True
        return context

def Test(request):
    print(request)
    return HttpResponse('<h1>Hello World!</h1>')