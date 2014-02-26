from django.db import models
from django.utils.translation import ugettext_lazy as _
from decimal import Decimal
from django.db.models.fields import DecimalField

    
'''
    The conference - an event.
'''
class Conference(models.Model):
    name = models.CharField(null = False, max_length = 150)
    description = models.TextField(null = False)
    registration_deadline = models.DateTimeField(null = False)
    open = models.BooleanField(default = False)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = _("Konferencija")
        verbose_name_plural = _("Konferencije")

'''
Discounts available for the conference (membership in an association, something else..)
'''
class Discount(models.Model):
    name = models.CharField(max_length = 500, null = False)
    #Discounts are in percents
    percent = models.IntegerField(null = False, default=10)
    #The discount is valid only for a specific conference
    conference = models.ForeignKey(Conference, null = True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = _("Popust")
        verbose_name_plural = _("Popusti")
    

'''
Conference package is a part of the conference, e.g.: lectures, workshops... 
'''
class ConferencePackage(models.Model):
    name = models.CharField(null = False, blank = False, max_length = 150)
    discounts = models.ManyToManyField(Discount, null = True, blank = True)
    conference = models.ForeignKey(Conference, null = False)
    
    class Meta:
        verbose_name = _("Konferencijski paket")
        verbose_name_plural = _("Konferencijski paketi")

    def __unicode__(self):
        return self.name

'''
    An option inside the Conference package
    e.g.: a set of workshops; set of lecture days, etc. 
'''
class ConferencePackageOption(models.Model):
    name = models.CharField(null = False, blank = False, max_length = 150)
    description = models.TextField(null = False, blank = False)
    package = models.ForeignKey(ConferencePackage, null = False)
    price = DecimalField(null = False, max_digits = 8, decimal_places = 2) 
    
    class Meta:
        verbose_name = _("Opcija paketa")
        verbose_name_plural = _("Opcije paketa")
        
    def __unicode__(self):
        return self.name
        



    