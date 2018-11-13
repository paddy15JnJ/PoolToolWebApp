# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
# import salesforce

class Contact(salesforce.models.Model):
    # Example that db_column is not necessary for most of fields even with
    # lower case names and for ForeignKey
    # print("IN MODELS")
    # print(models)
    LastName = models.CharField("Name",max_length=80)
    Email = models.EmailField("Email", max_length=80)
    def __str__(self):
        return self.LastName
