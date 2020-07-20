# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class students(models.Model):
    stuid = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    chinese = models.IntegerField(default=0)
    math = models.IntegerField(default=0)
    english = models.IntegerField(default=0)
    physics = models.IntegerField(default=0)
    chemistry = models.IntegerField(default=0)
    scoresum = models.IntegerField(default=0)
    def __unicode__(self):
        return self.name