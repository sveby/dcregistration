from django.db import models
from django.utils.translation import ugettext_lazy as _
from Conference import models as Conference


#A person registering for the event
class Person(models.Model):
    name = models.TextField(null = False, blank = False)
    last_name = models.TextField(null = False, blank = False)
    oib = models.CharField(max_length = 13, null = True, blank=True)
    address = models.TextField(null = False, blank = False)
    email = models.EmailField(null = False, blank = False)
    
    def __unicode__(self):
        return self.name + ' ' + self.last_name
    
    class Meta:
        verbose_name = _("Osoba")
        verbose_name_plural = _("Osobe")


#Simple person model to be used for list of people coming from a single company
class PersonSimple(models.Model):
    name = models.TextField(null = False, blank = False)
    last_name = models.TextField(null = False, blank = False)
    
    def __unicode__(self):
        return self.name + ' ' + self.last_name
    
    class Meta:
        verbose_name = _("Osoba")
        verbose_name_plural = _("Osobe")
    

#A company used in registration
class Company(models.Model):
    name = models.TextField(null = False, blank = False)
    oib = models.CharField(max_length = 13, null = True, blank=False)
    address = models.TextField(null = False, blank = False)
    email = models.EmailField(null = False, blank = False)
    people = models.ManyToManyField(PersonSimple, null = False)
    
    def __unicode__(self):
        return self.name + ' ' + self.last_name
    
    class Meta:
        verbose_name = _("Tvrtka")
        verbose_name_plural = _("Tvrtke")
        
        
#Model that will store our actual registrations and connect it all together
class Registration(models.Model):
    people = models.ManyToManyField(Person)
    company = models.ForeignKey(Company)
    conference = models.ForeignKey(Conference.Conference)
    discounts = models.ManyToManyField(Conference.Discount)
    conference_package = models.ForeignKey(Conference.ConferencePackage)
