from django.db import models


class Entry(models.Model):
    title = models.CharField(max_length=255)
    note = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        verbose_name = "Entries"
