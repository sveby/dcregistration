from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

'''
Popust na clanstvo ili tako nesto
'''
class Discount(models.Model):
    name = models.CharField(max_length = 500, null = False)
    percent = models.IntegerField(null = False, default=10)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = _("Popust")
        verbose_name_plural = _("Popusti")
    
'''
    Odabir izmedu npr. 1 dan, 2 dana, 1 dan + radionice, 
    2 dana + radionice, radionice
'''
class ConferencePackage(models.Model):
    name = models.CharField(null = False, blank = False)
    discounts = models.ManyToManyField(Discount, null = True)
    
    class Meta:
        verbose_name = _("Konferencijski paket")
        verbose_name_plural = _("Konferencijski paketi")
        
    def __unicode__(self):
        return self.name
        

'''
    Konferencija je pojedinacan događaj.
'''
class Conference(models.Model):
    name = models.CharField(null = False)
    description = models.TextField(null = False)
    registration_deadline = models.DateTimeField(null = False)
    open = models.BooleanField(default = False)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = _("Konferencija")
        verbose_name_plural = _("Konferencije")

    

    