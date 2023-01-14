from django.urls import path
from apps.buildings.views import building_detail

urlpatterns = [
    path('<int:id>/', building_detail, name='building_detail'),
]
