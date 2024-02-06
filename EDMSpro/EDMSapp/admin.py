from django.contrib import admin

# Register your models here.
from .models import EDMSmodel
from .models import Emp_address




class EDMSReorderFields(admin.ModelAdmin):
    fields = ['name', 'roll_no','email','manager']    # list of fields with the order of fields that are required to be displayed
    search_fields = ['roll_no'] #use for search bar
    list_display = ('name', 'email','id') #use to show number not only object 1,obj2 etc
    list_filter = ("roll_no", )
    
# registering the Question model
admin.site.register(EDMSmodel, EDMSReorderFields)

class emp_add(admin.ModelAdmin):
    fields = ['state','city','pin']
    search_fields = ['pin']
    list_display = ('id','emp_model_id','state','city','pin')
    list_filter = ('state',)
admin.site.register(Emp_address , emp_add)


