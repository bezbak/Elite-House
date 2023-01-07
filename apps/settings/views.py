from django.shortcuts import render
from apps.settings.models import Settings, Slider

# Create your views here.

def index(request):
    setting = Settings.objects.latest('id')
    slider = Slider.objects.all()
    context = {
        'setting':setting,
        'slider':slider,
    }
    return render(request, 'index.html', context)