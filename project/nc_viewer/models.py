from django.db import models


class Entrant(models.Model):
    name = models.TextField()
    organization = models.TextField()
    twitter = models.TextField()
    country = models.TextField()


class Entry(models.Model):
    url = models.URLField()
    invalid = models.BooleanField(default=False)
    title = models.TextField(default="")
    what = models.TextField(default="")
    who_else = models.TextField(default="")
    description = models.TextField(default="")
    why = models.TextField(default="")
    who = models.TextField(default="")
    already_done = models.TextField(default="")
    sustain = models.TextField(default="")

    amount = models.TextField(default="")  # Maybe they're asking for lots?
    time = models.TextField(default="")
    total_cost = models.TextField(default="")

    # Allow to be empty, because some people can't fill out a form
    entrant = models.ForeignKey(Entrant, null=True, blank=True)

