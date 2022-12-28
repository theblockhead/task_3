from django.contrib import admin

# Register your models here.
from .models import Profile
#, Matchedlist, Request

admin.site.register(Profile)
# admin.site.register(Matchedlist)
# admin.site.register(Request)