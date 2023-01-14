from django.shortcuts import render
from apps.buildings.models import Building
from apps.settings.models import Settings
# Create your views here.
def building_detail(request, id):
    setting = Settings.objects.latest('id')
    building = Building.objects.get(id = id)
    context = {
        'setting': setting,
        'building': building,
    }
    return render(request, 'page-project-detail-2.html', context)

def building_index(request):
    buildings = Building.objects.all()