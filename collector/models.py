from django.db import models

class SignUp(models.Model):
    full_name = models.CharField(max_length=120)
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.full_name