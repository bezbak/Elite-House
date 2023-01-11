from django.urls import path
from apps.team.views import team_index

urlpatterns = [
    path('', team_index, name='team_index')
]
