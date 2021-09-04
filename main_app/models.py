from django.db import models
from django.contrib.auth.models import User


class ProfileModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    phone = models.IntegerField()

    def __str__(self):
        return self.name
