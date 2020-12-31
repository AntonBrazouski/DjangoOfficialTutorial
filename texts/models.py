from django.db import models

class Message(models.Model):
    text = models.CharField(max_length=10)
    key = models.SmallIntegerField()

    def __str__(self):
        return self.text
