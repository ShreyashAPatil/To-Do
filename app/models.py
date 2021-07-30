from django.db import models

# Create your models here.

class blog(models.Model):
    title=models.TextField()
    content=models.TextField()
    date=models.DateField()
   

    def __str__(self):
        return self.title