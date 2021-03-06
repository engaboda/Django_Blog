from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.


class Posts(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(null=True , blank=True, height_field='height_field', width_field='width_field' )   #max_length=120
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField() #max_length=120
    updated = models.DateTimeField(auto_now=True,auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)
    
    
    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:detials" , kwargs={"id":self.id})