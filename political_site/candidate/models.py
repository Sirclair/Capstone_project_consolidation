from django.db import models

# Create your models here.


class Candidate(models.Model):
    """
    Model representing a political candidate.

    Attributes:
        name (str): The name of the candidate.
        party (str): The political party of the candidate.
        description (str): A brief description of the candidate.
        vote_count (int): The number of votes the candidate has received.
    """
    name = models.CharField(max_length=100)
    party = models.CharField(max_length=100)
    description = models.TextField()
    vote_count = models.IntegerField(default=0)

    def __str__(self):
        """
        Returns the string representation of the candidate.

        Returns:
            str: The name of the candidate.
        """
        return self.name
