from django.shortcuts import render, redirect
from Confreg.forms import PersonModelForm, CompanyModelForm
from django.http.response import HttpResponse
from Conference.models import *
from django.forms.formsets import formset_factory
from Confreg.models import Registration


'''
If only one event accepts registrations, redirect, otherwise, 
show list of events or info that no registrations are possible
''' 
def index(request):
    available_conferences = Conference.objects.filter(open = True)
    if len(available_conferences) == 1:
        return redirect('reg:show_registration', conference_id = available_conferences[0].id)
    
    return HttpResponse("Nema konferencije dostupne za prijavu.")

    
    
#Show the registration first screen
def show_registration(request, conference_id):
    conference = Conference.objects.get(id=conference_id)
    data = {'step_1':True, 'conference':conference}
    data['conference_packages'] = ConferencePackage.objects.filter(conference=conference.id)
    
    # we need to add the fields to select package options to a person formset here...
    
    if request.method == "POST":
        if request.POST.get('company_submit')=="OK!":
            f = data['company_form'] = CompanyModelForm(request.POST)
            data['person_form'] = PersonModelForm()
            data['show_form'] = "company"
            
            if f.is_valid():
                #save registration object, save reg. id to session 
                request.session['registration'] = 1
                return redirect('reg:register_company', conference_id = conference_id)
                
        elif request.POST.get('person_submit')=="OK!":
            f = data['person_form'] = PersonModelForm(request.POST)
            data['company_form'] = CompanyModelForm()
            data['show_form'] = "personal"
            
            if f.is_valid():
                #save registration object, save reg. id to session
                request.session['registration'] = 2
                return redirect('reg:register_person', conference_id = conference_id)
    else:
        data['person_form'] = PersonModelForm()
        data['company_form'] = CompanyModelForm()
        data['show_form'] = "personal"
        
    return render(request, "registration_form.html", data)


#TODO: implement us:
def register_person(request, conference_id):
    #create formset for multiple people
    #save data received up until now
    #do something smart
    return HttpResponse("person")
def register_company(request, conference_id):
    #create formset for multiple people
    #save data received up until now
    #registration.conference = 
    #do something smart
    return HttpResponse("company")


#def finalize_registration(request, registration_id):
    #hanlde form to finalize registration