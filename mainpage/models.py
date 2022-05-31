from django.db import models

class Apply(models.Model):
    name = models.TextField()
    phonenumber = models.TextField()
    koreandance = models.TextField(null=True)
    PIagree= models.TextField(null=True)
    how_think = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Email(models.Model):
    email = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
