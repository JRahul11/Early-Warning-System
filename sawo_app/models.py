from django.db import models


class Config(models.Model):
    api_key = models.CharField(max_length=200)
    identifier = models.CharField(max_length=100, choices=[(
        "email", "Email"), ("phone_number_sms", "Phone")])
