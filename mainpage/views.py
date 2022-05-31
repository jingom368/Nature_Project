from django.shortcuts import render
from rest_framework.views import APIView
from .models import Apply, Email
from django.utils import timezone
from django.http import HttpResponseRedirect



class Personal_Information(APIView):
    def get(self, request):
        return render(request, "nature_project/seoul_forest.html")

    def post(self, request):
        if request.method=='POST' and 'contact-submit-button' in request.POST:
            new_post = Apply()
            new_post.name = request.POST["name"]
            new_post.phonenumber = request.POST["phonenumber"]
            new_post.koreandance = request.POST.getlist('answer_1[]')
            new_post.PIagree = request.POST.getlist('answer_2[]')
            new_post.how_think = request.POST.get('how-think')
            new_post.created_at = timezone.now()
            new_post.save()

        elif request.method=='POST' and 'footer-submit-button' in request.POST:
            dancer_post = Email()
            dancer_post.email = request.POST["email"]
            dancer_post.save()

        return HttpResponseRedirect("/")

def seoul_forest_read(request):
    personal_list = Apply.objects.all().order_by("-pk")
    dancer_email_list = Email.objects.all().order_by("-pk")
    context = {
        "personal_list": personal_list,
        "dancer_email_list": dancer_email_list
    }
    return render(request, "nature_project/seoul_forest_read.html", context)