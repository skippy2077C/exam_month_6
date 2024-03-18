from django.shortcuts import render
from .models import Pupils 
# Create your views here.



def pupils_list(request):
    pupils_list = Pupils.objects.all()
    return render(request, 'pupils_templates/home.html', {'pupils_list': pupils_list})

def pupils_detail(request , id ):
    pupils_detail = Pupils.objects.get(pk=id )  
    print(pupils_detail.mark1)
    return render(request, 'pupils_templates/pupil_detail.html', {'pupils_detail': pupils_detail})  





























# def Themes_list(request):
#     themes = Themes.objects.all()
#     return render(request, 'themes_templates/home.html', {'themes': themes})




# def pupils_list_view(request):
#     pupils = Pupils.objects.all()
#     return render(request, 'pupils/pupils_list.html', {'pupils': pupils})
    


