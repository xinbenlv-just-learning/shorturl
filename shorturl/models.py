from django.db import models
import datetime
class Sue(models.Model):
  original = models.CharField(max_length=8192)
  def __unicode__(self):  
    return self.original
  class Meta:
    ordering = ['original']

