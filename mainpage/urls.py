from django.urls import path
from .views import Personal_Information
from .views import seoul_forest_read, Program


urlpatterns = [
    path('', Personal_Information.as_view()),
    path('program', Program.as_view()),
    path('read',seoul_forest_read),
]