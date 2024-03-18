from django.db import models

# Create your models here.


class Themes(models.Model):
    theme_name = models.CharField(max_length=100 )
    theme_detail = models.CharField(max_length=300)

    class Meta:
        db_table = 'themes'
        verbose_name = 'mavzular'

    def  __str__(self):
        return self.theme_name
