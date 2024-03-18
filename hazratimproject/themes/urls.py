from django.urls  import  path , include 
from django.contrib import admin 

from .views import Themes_list , theme_detail , theme_create  ,  theme_edit , theme_delete 




urlpatterns = [
    path('', Themes_list ),
    path('<int:pk>' , theme_detail )  , 
    path('edit/<int:pk>' , theme_edit  , name='edit_theme' )  , 
    path('add/', theme_create , name='theme_create')  , 
    path('delete/<int:pk>', theme_delete , name='theme_delete')
    
]   




