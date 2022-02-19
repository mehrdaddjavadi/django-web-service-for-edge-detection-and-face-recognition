from django.db import models

# Create your models here.
class FaceRecognition(models.Model):
    id = models.AutoField(primary_key=True)
    record_date = models.DateTimeField(auto_now_add=True)
    image= models.ImageField( upload_to='images/', height_field=None, width_field=None, max_length=None)
    # T_parameters =models.DecimalField(max_digits=5, decimal_places=2)
    # V_parameters =models.DecimalField(max_digits=5, decimal_places=2)
    # C_parameters =models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return str(self.record_date)
    
    
    
   