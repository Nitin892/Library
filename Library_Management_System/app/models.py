from django.db import models
from django.contrib.auth.models import User


from django.db import models

# Create your models here.


class Book(models.Model):
    name=models.CharField(max_length=30)
    desc=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name