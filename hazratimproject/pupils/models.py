from django.shortcuts import render , get_list_or_404 , redirect 
from django.db import models

# Create your models here.
class Pupils(models.Model):
    fullname = models.CharField(max_length=255, verbose_name='fullname'  )  
    profile_image = models.CharField(max_length=255 ,  verbose_name='profile_image' )
    mark1 = models.IntegerField( verbose_name='mark1',default=1 )
    mark2 = models.IntegerField( verbose_name='mark2',default=1 )
    mark3 = models.IntegerField( verbose_name='mark3',default=1 )
    mark4 = models.IntegerField( verbose_name='mark4',default=1 )
    mark5 = models.IntegerField( verbose_name='mark5',default=1 )
    mark6 = models.IntegerField( verbose_name='mark6' , default=1 )

    class Meta:
        db_table = 'pupils'
        verbose_name = 'pupil'
        ordering = ('id',  )

    def __str__(self) -> str:
        return self.fullname
