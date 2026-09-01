from django.db import models

class UserProfile(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    subscribers = models.IntegerField(default=0)

    def __str__(self):
        return self.username
