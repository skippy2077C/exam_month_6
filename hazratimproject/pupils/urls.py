from django.urls import path
 
from .views  import pupils_list  , pupils_detail


urlpatterns = [
    path('' , pupils_list  ) , 
    path('<int:id>'  , pupils_detail   ) 
]