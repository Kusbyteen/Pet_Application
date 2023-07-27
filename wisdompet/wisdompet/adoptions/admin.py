from django.contrib import admin
from django.contrib.admin.decorators import register

# Register your models here.

from .models import Pet

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['name','species','breed','age','sex']