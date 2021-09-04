from django.db import models
from django.contrib.auth.models import User


class MedModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pill_name = models.CharField(max_length=20)
    pill_dosage = models.IntegerField(default=0)
    pill_time = models.TimeField(auto_now_add=False)
    pill_frequency = models.CharField(max_length=20)

    def __str__(self):
        return self.pill_name


class ProfileModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    phone = models.IntegerField(default=-1)

    def __str__(self):
        return self.name
