from django.shortcuts import render
from rest_framework.views import APIView

class Seoul_forest(APIView):
    def get(self, request):
        return render(request, "nature_project/seoul_forest.html")