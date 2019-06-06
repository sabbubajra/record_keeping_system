from django.db import models
from datetime import datetime

# Create your models here.
class Notice(models.Model):
    title=models.CharField(max_length=500)
    description=models.TextField(blank=True,max_length=2000)
    image=models.ImageField(upload_to='Notice',blank=True)
    created_date = models.DateTimeField('date created', default=datetime.now())

    def __str__(self):
        return self.title