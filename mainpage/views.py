from django.shortcuts import render
from rest_framework.views import APIView
from .models import Apply, Contact, Select
from django.utils import timezone
from django.http import HttpResponseRedirect



class Personal_Information(APIView):
    def get(self, request):
        return render(request, "nature_project/seoul_forest.html")

    def post(self, request):
        if request.method=='POST' and 'contact-submit-button' in request.POST:
            new_post = Apply()
            new_post.name = request.POST["name"]
            new_post.phonenumber_1 = request.POST["phonenumber_1"]
            new_post.koreandance = request.POST.getlist('answer_1[]')
            new_post.PIagree = request.POST.getlist('answer_2[]')
            # new_post.fruit = request.POST.get('fruit')
            new_post.how_think = request.POST.get('how_think')
            new_post.created_at = timezone.now()
            new_post.save()

        elif request.method=='POST' and 'footer-submit-button' in request.POST:
            dancer_post = Contact()
            dancer_post.contact = request.POST["contact"]
            dancer_post.save()

        return HttpResponseRedirect("/")

def seoul_forest_read(request):
    personal_list = Apply.objects.all().order_by("-pk")
    dancer_phonenumber_list = Contact.objects.all().order_by("-pk")
    context = {
        "personal_list": personal_list,
        "dancer_phonenumber_list": dancer_phonenumber_list
    }
    return render(request, "nature_project/seoul_forest_read.html", context)

class Program(APIView):
    def get(self, request):
        return render(request, "nature_project/program.html")

    def post(self, request):
        if request.method=='POST' and 'event_list_button' in request.POST:
            new_post2 = Select()
            new_post2.select_1 = request.POST.get('select_1')
            new_post2.select_2 = request.POST.get('select_2')
            new_post2.select_3 = request.POST.get('select_3')
            new_post2.select_4 = request.POST.get('select_4')
            new_post2.select_5 = request.POST.get('select_5')            
            new_post2.event_name = request.POST["event_name"]
            new_post2.event_phonenumber = request.POST["event_phonenumber"]
            new_post2.event_PIagree = request.POST.getlist('event_answer[]')
            new_post2.event_created_at = timezone.now()
            new_post2.save()

        elif request.method=='POST' and 'footer-submit-button2' in request.POST:
            dancer_post = Contact()
            dancer_post.contact = request.POST["contact"]
            dancer_post.save()

        return HttpResponseRedirect("/program")

def seoul_forest_event_read(request):
    event_list = Select.objects.all().order_by("-pk")
    context = {
        "event_list": event_list,
    }
    return render(request, "nature_project/seoul_forest_event.html", context)
