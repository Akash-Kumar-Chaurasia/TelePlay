from enum import unique
from django.db import models

class email(models.Model):
    user_mail = models.EmailField()

    def __str__(self):
       return self.user_mail