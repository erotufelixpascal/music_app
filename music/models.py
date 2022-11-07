from django.db import models

# Create your models here.
class Music(models.Model):
    artist= models.CharField(max_length= 500)
    title= models.CharField(max_length=500)
    album =models.ForeignKey('Album',on_delete=models.SET_NULL,null=True,blank=True)
    time_length=models.DecimalField(blank=True,max_digits=20,decimal_places=2)
    audio_file=models.FileField(upload_to='music')
    cover_image= models.ImageField(upload_to='music_image/')

#representing the class
    def save(self,*args, **kwargs):
        if not self.time_length:
            #logic for getting music length
            pass
        return super().save(*args, **kwargs) 

class Album(models.Model):
    name=models.CharField(max_length=500)


    
