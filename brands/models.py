# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Info(models.Model):
    brand = models.CharField(max_length=250, default='')
        # The brand the data belongs to e.g. cocacola
    owner = models.ForeignKey('auth.User', related_name='info', on_delete=models.PROTECT) # The person who entered the data is the logged in user(owner)
          # Once the user is deleted the records on data should still have the name
    interviewee = models.CharField(max_length=100, default='')
    favorite = models.CharField(max_length=150, default='')
    disliked = models.CharField(max_length=150, default='')
    reason = models.TextField(default='', blank=True) 
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name
