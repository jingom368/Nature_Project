from django.shortcuts import render
from rest_framework.views import APIView
from .models import Apply
from django.utils import timezone
from django.http import HttpResponseRedirect

class Seoul_forest(APIView):
    def get(self, request):
        return render(request, "nature_project/seoul_forest.html")

    def post(self, request):
        new_post = Apply()
        new_post.name = request.POST["name"]
        new_post.phonenumber = request.POST["phonenumber"]
        new_post.koreandance = request.POST.getlist('answer_1[]')
        new_post.PIagree = request.POST.getlist('answer_2[]')
        # new_post.select = request.POST.get('how-think')
        new_post.created_at = timezone.now()
        new_post.save()

        return HttpResponseRedirect("/mainpage/seoul_forest/")