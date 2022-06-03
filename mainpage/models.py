from unicodedata import category
from django.db import models

class Apply(models.Model):
    name = models.TextField()
    phonenumber_1 = models.TextField()
    koreandance = models.TextField(null=True)
    PIagree= models.TextField(null=True)
    category_fruit = (('푸릇푸릇한 자연을 좋아해서.','푸릇푸릇한 자연을 좋아해서.'),('푸릇푸릇한 자연을 좋아해서.','아무런 이유없이도 산책을 즐겨해요.'),('생각(고민)의 정리가 필요할 때.','생각(고민)의 정리가 필요할 때.'),('스트레스를 해소하기 위해서.','스트레스를 해소하기 위해서.'))
    fruit = models.CharField(null=True, max_length=30, choices=category_fruit)
    category_Choices = (('푸릇푸릇한 자연을 좋아해서.','푸릇푸릇한 자연을 좋아해서.'),('푸릇푸릇한 자연을 좋아해서.','아무런 이유없이도 산책을 즐겨해요.'),('생각(고민)의 정리가 필요할 때.','생각(고민)의 정리가 필요할 때.'),('스트레스를 해소하기 위해서.','스트레스를 해소하기 위해서.'))
    how_think = models.CharField(null=True, max_length=30, choices=category_Choices)
    created_at = models.DateTimeField(auto_now_add=True)

class Contact(models.Model):
    contact = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
