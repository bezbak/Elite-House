from django.shortcuts import render
from apps.settings.models import Settings
from apps.team.models import Team
# Create your views here.
def team_index(request):
    setting = Settings.objects.latest('id')
    teams = Team.objects.all()
    context = {
        'setting':setting,
        'teams': teams
    }
    return render(request, 'team_index.html', context)