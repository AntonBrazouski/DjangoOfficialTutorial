from django.db import models
from datetime import timedelta
from django.utils import timezone

class Ask(models.Model):
    question = models.TextField(max_length=10)
    datestamp = models.DateTimeField('timestamp')

    def __str__(self):
        return self.question

    def is_recent(self):
        return self.datestamp > timezone.now() - timedelta(minutes=2)


class Option(models.Model):
    ask = models.ForeignKey(Ask, on_delete=models.CASCADE)
    option_text = models.TextField(max_length=10)
    counts = models.IntegerField(default=1)

    def __str__(self):
        return str(self.counts)
