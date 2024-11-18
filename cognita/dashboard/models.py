from django.db import models

# Create your models here.
class Entries(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    author = models.CharField(max_length=255)
    is_published = models.BooleanField()
    time_create = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + ' - ' + self.author