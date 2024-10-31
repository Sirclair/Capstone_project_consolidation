from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Candidate

# Register the Candidate model
admin.site.register(Candidate)
