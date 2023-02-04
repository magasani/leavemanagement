from django.contrib import admin

# Register your models here.
from . models import Leave,Employee_Detail

admin.site.register(Employee_Detail)
admin.site.register(Leave)

