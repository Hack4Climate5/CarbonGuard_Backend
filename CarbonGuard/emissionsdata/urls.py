from django.urls import path
from .views import EmissionsDataListView

urlpatterns = [
    path('emissionsdata/', EmissionsDataListView.as_view(),name='emissions_data'),
]