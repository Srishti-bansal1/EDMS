from django.db import models

# Create your models here.
class EDMSmodel(models.Model):
    name = models.CharField(max_length = 100)
    roll_no = models.IntegerField()
    email = models.EmailField()
    manager = models.ForeignKey( 'self' , null= True, on_delete = models.CASCADE)
    
class Emp_address(models.Model):
    emp_model = models.ForeignKey(EDMSmodel, default = None,  on_delete = models.CASCADE, related_name='address' )
    state = models.CharField(max_length = 100 , default = None)
    city = models.CharField(max_length = 100 , default =None)
    pin = models.IntegerField(default = None)
