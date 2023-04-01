from django.db import models

# Create your models here.

class Menu(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    menu_name = models.CharField(max_length=255)
