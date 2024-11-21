from django.db import models

class Entries(models.Model):
    """
    The main table in the database.
    Which stores all user records...
    """

    name = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    author = models.CharField(max_length=255)
    is_published = models.BooleanField()
    time_create = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + ' - ' + self.author