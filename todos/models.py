from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class todo(models.Model):
    #noteOwner = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    title = models.TextField()
    content = models.TextField()
