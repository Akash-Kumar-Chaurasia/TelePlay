from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models


# Create your forms here.
class UserRegistrationForm(UserCreationForm):
    email = models.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']