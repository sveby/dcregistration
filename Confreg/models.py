from django.db import models
from django.utils.translation import ugettext_lazy as _
from Conference import models as Conference
from datetime import date, datetime

        
#Model that will store our actual registrations and connect it all together
class Registration(models.Model):
    conference = models.ForeignKey(Conference.Conference)
    time_registered = models.DateTimeField(null = False, default = datetime.now())
    #TODO: add data about user: IP, user agent ... 

#A person registering for the event
class Person(models.Model):
    name = models.TextField(null = False, blank = False)
    last_name = models.TextField(null = False, blank = False)
    oib = models.CharField(max_length = 13, null = True, blank=True)
    address = models.TextField(null = False, blank = False)
    email = models.EmailField(null = False, blank = False)
    phone = models.CharField(max_length=20)
    registration = models.ForeignKey(Registration, null = False)
    conference_options = models.ManyToManyField(Conference.ConferencePackageOption)
    discounts = models.ManyToManyField(Conference.Discount)
    
    def __unicode__(self):
        return self.name + ' ' + self.last_name
    
    class Meta:
        verbose_name = _("Osoba")
        verbose_name_plural = _("Osobe")


#A company used in registration
class Company(models.Model):
    name = models.TextField(null = False, blank = False)
    oib = models.CharField(max_length = 13, null = False, blank=False)
    address = models.TextField(null = False, blank = False)
    email = models.EmailField(null = False, blank = False)
    registration = models.ForeignKey(Registration, null = False)
    
    def __unicode__(self):
        return self.name + ' ' + self.last_name
    
    class Meta:
        verbose_name = _("Tvrtka")
        verbose_name_plural = _("Tvrtke")
        

    
