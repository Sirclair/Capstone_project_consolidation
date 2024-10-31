from django.db import models

# Create your models here.

class Candidate(models.Model):
    """
    Model representing a political candidate.

    Attributes:
        name (str): The name of the candidate.
        party (str): The political party the candidate belongs to.
        description (str): A brief description of the candidate.
        vote_count (int): The number of votes the candidate has received. Defaults to 0.
    """
    name = models.CharField(max_length=100)
    party = models.CharField(max_length=100)
    description = models.TextField()
    vote_count = models.IntegerField(default=0)

    def __str__(self):
        """
        String for representing the Candidate object (in Admin site etc.).
        """
        return self.name
