from django.urls import path
from .views import Personal_Information, Program
from .views import seoul_forest_read, seoul_forest_event_read 


urlpatterns = [
    path('', Personal_Information.as_view()),
    path('program', Program.as_view()),
    path('read',seoul_forest_read),
    path('event', seoul_forest_event_read)
]