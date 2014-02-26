from django.contrib import admin
from .models import *

admin.site.register(Conference)
admin.site.register(Discount)
admin.site.register(ConferencePackage)
admin.site.register(ConferencePackageOption)