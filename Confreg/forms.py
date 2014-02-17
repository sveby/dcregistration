# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _
from Confreg import models


'''
    TODO: Na koji način napraviti dinamicnu formu s arbitrary brojem osoba
    koje korisnik dodaje ili uklanja po zelji, te kad submita da se ta 
    forma validira?
'''
class RegistrationForm(forms.Form):
    name = forms.CharField(max_length = 150)
    last_name = forms.CharField(max_length = 150)
    description = forms.Textarea()
