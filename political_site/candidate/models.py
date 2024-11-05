from django.db import models

# Create your models here.


class Candidate(models.Model):
    name = models.CharField(max_length=100)
    party = models.CharField(max_length=100)
    description = models.TextField()
    vote_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name
