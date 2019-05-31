from django.db import models

# Create your models here.
class Weather_data(models.Model):
    wd_id = models.AutoField(primary_key=True)
    wd_humidity = models.CharField(max_length = 10)
    wd_temp = models.CharField(max_length = 10)
    wd_date =  models.DateTimeField('date published')
    
    def __str__(self):
        return self.wd_id