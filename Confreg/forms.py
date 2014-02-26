# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _
from Confreg.models import *
from Conference.models import *
from django.forms.formsets import BaseFormSet


# adding fields for options to person formset:
class BaseArticleFormSet(BaseFormSet):
    def add_fields(self, form, index):
        super(BaseArticleFormSet, self).add_fields(form, index)
        #get options per packages
        # add to formset: (for u for petlji)
        form.fields["option"] = forms.CharField()

class PersonForm(forms.Form):
    name = forms.CharField(max_length = 150)
    last_name = forms.CharField(max_length = 150)
    oib = forms.CharField(max_length = 13)
    phone = forms.CharField(max_length = 30)
    email = forms.EmailField(required = False)
    
class PersonModelForm(forms.ModelForm):
    class Meta:
        model = Person
        exclude = ['registration']
        widgets = {'name':forms.TextInput, 'last_name':forms.TextInput, 'address':forms.Textarea(attrs={'cols': 25, 'rows': 4})}
    
        
    
class CompanyModelForm(forms.ModelForm):
    class Meta:
        model = Company
        exclude = ['registration']
        widgets = {'name':forms.TextInput, 'address':forms.Textarea(attrs={'cols': 25, 'rows': 4})}

class ConferenceOptionForm(forms.ModelForm):
    class Meta:
        model = ConferencePackageOption
        exclude = ['package']
        
class BlaForm(PersonModelForm):
    def setConference(self, conference_id):
        self.conference_id = conference_id
    #additional fields:
    nekaj = forms.CharField(max_length = 10)
    
    #options = forms.ChoiceField(required = True, choices=getConfOptions())
    
'''
    TODO: Na koji način napraviti dinamicnu formu s arbitrary brojem osoba
    koje korisnik dodaje ili uklanja po zelji, te kad submita da se ta 
    forma validira?
'''
class RegistrationForm(forms.Form):
    name = forms.CharField(max_length = 150)
    last_name = forms.CharField(max_length = 150)
    description = forms.Textarea()
