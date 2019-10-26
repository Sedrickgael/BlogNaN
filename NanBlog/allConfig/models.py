from django.db import models
from tinymce import HTMLField
# Create your models here.

class AllInfo(models.Model):
    titre = models.CharField(max_length=250)
    description = models.TextField()
    icon = models.CharField(max_length=250)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

class HeaderFront(models.Model):
    logo = models.ImageField(upload_to='entreprise/')
    image = models.ImageField(upload_to='blog/')
    titre = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

class FooterFront(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

class Social(models.Model):
    choice=[('FB','facebook'),('TW','twitter'),('INS','instagram'),('GOO','google')]
    name = models.CharField(max_length=100,choices=choice)
    lien = models.URLField(max_length=200)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    
    @property
    def font(self):
        print(self.name)
        if self.name == 'FB':
            font = 'icon-facebook'
        elif self.name == 'TW':
            font ='icon-twitter'
        elif self.name == 'INS':
            font ='icon-instagram'
        elif self.name == 'GOO':
            font ='icon-google-plus'
        return font
    class Meta:
        verbose_name = "Social"
        verbose_name_plural = "Socials"

    def __str__(self):
        return '{}'.format(self.name)

class LocationMap(models.Model):
    map = models.URLField()
    laltitude=models.DecimalField(max_length=10,decimal_places=4,max_digits=10)
    longitude=models.DecimalField(max_length=10,decimal_places=4,max_digits=10)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

class Copyright(models.Model):
    titre = HTMLField('content')
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

class Instagram(models.Model):
    image = models.ImageField(upload_to='instagram/')
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)