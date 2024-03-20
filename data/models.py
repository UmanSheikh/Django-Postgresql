from django.db import models

# Create your models here.
class Office(models.Model):
    id = models.IntegerField(primary_key=True)
    dep = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.dep}'
