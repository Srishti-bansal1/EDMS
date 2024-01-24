from django.db import models

# Create your models here.
class EDMSmodel(models.Model):
    name = models.CharField(max_length = 100)
    roll_no = models.IntegerField()
    email = models.EmailField()
    manager = models.ForeignKey( 'self' , null= True, on_delete = models.CASCADE)
    
