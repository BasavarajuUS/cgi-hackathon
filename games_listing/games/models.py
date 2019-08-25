# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Game(models.Model):
    title = models.CharField(max_length=250, verbose_name='Game title', default='',
                             error_messages={'null': 'Game Title is required'})
    platform = models.CharField(max_length=100, null=False, blank=False,
                                error_messages={'null': 'Game Platform is required'})

    score = models.FloatField(max_length=10, null=False, blank=False, default=0.0)
    genre = models.CharField(max_length=100, null=True, blank=True)

    CHOICES = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
    editors_choice = models.CharField(max_length=1, null=False, blank=False, choices=CHOICES)

    class Meta:
        verbose_name_plural = 'Games'

    def __str__(self):
        return self.title

    def as_json(self):
        return {
            "title": self.title,
            "platform": self.platform,
            "score": self.score,
            "genre": self.genre,
            "editors_choice": self.get_editors_choice_display(),
        }