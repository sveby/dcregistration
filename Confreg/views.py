from django.shortcuts import render
from Confreg.forms import RegistrationForm
from django.template import loader
from django.http.response import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("Bla")

def show_registration(request, conference_id):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
    else:
        form = RegistrationForm()
    
    return render(request, "registration_form.html", {
                                                      'form':form,
                                                      'conference_id':conference_id,
                                                      })
    