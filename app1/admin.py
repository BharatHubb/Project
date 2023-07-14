from django.contrib import admin
from .models import emp
# Register your models here.
class empadmin(admin.ModelAdmin):
    list_display = ['name',"joining_date"]
admin.site.register(emp,empadmin)