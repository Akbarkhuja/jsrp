from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

class GeneralAdmin(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name")

admin.site.register(MyUser, GeneralAdmin)
admin.site.register(Applicant)
admin.site.register(Recruiter)