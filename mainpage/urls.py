from django.urls import path
from .views import Seoul_forest

urlpatterns = [
    path('seoul_forest/', Seoul_forest.as_view())
]