from django.db import models
import pprint
import re  # noqa: F401

import six


class Empleo(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


 