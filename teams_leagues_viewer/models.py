from django.db import models


class League(models.Model):

    objects = models.Manager()

    abbr = models.CharField(max_length=10)
    name = models.CharField(max_length=200)

    def __repr__(self):
        return f"{self.abbr} -- {self.name}"


class Team(models.Model):

    objects = models.Manager()

    abbr = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    league = models.ForeignKey(League, on_delete=models.CASCADE)

    def __repr__(self):
        return f"{self.abbr} -- {self.name}"
