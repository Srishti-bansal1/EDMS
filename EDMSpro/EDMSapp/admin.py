from django.contrib import admin

# Register your models here.
from .models import EDMSmodel




class EDMSReorderFields(admin.ModelAdmin):
    fields = ['name', 'roll_no','email','manager']    # list of fields with the order of fields that are required to be displayed
    search_fields = ['roll_no'] #use for search bar
    list_display = ('name', 'email','manager') #use to show number not only object 1,obj2 etc
    list_filter = ("roll_no", )
    
# registering the Question model
admin.site.register(EDMSmodel, EDMSReorderFields)


