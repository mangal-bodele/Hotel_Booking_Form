from django.db import models


class Hotel(models.Model):
    hotel_name = models.CharField(max_length=20,null=True)
    person_name = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=20)
    check_in = models.DateTimeField(auto_now_add=True)
    check_out = models.DateTimeField(auto_now=True)
    phone = models.IntegerField()
    email = models.EmailField()
