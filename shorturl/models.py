from django.db import models
from django.contrib.auth.models import User
import datetime
class Sue(models.Model):
  original = models.CharField(max_length=8192)
  short = models.CharField(max_length=40)
  owner = models.ForeignKey(User, null=True, blank=True, related_name="%(app_label)s_%(class)s_related_"+"owner")
  created_date = models.DateTimeField(null=True,blank=True, auto_now_add=True)
  count = models.PositiveSmallIntegerField(null=True,blank=True)
  def __unicode__(self):  
    return self.short
  class Meta:
    ordering = ['original']

