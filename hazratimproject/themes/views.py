from django.shortcuts import render, redirect , get_object_or_404
from .models import Themes 

def Themes_list(request):
    themes = Themes.objects.all()
    return render(request, 'themes_templates/home.html', {'themes': themes})

def theme_detail(request, pk):
    theme_detail = Themes.objects.filter(pk=pk)
    return render(request, 'themes_templates/theme_detail.html', {'theme_detail': theme_detail})

def theme_create(request):
    if request.method == 'POST':
        theme_name = request.POST['theme_name']
        theme_detail = request.POST['theme_detail']
        
        new_theme = Themes(theme_name=theme_name, theme_detail=theme_detail)
        new_theme.save()
        return redirect('theme_create'  )
    else:
        return render(request, 'themes_templates/add_theme.html')

def home(request):
    return render(request, 'index.html' ,  {'home':home})    
    
def theme_edit(request , pk ):
    this_theme = Themes.objects.get(id=pk) 
    if request.method ==  'POST':
         
         this_theme.theme_name = request.POST['theme_name']
         this_theme.theme_detail = request.POST['theme_detail']
         this_theme.save()
         return redirect('theme_detail', pk=this_theme.pk)
    else:
        return render(request, 'themes_templates/edit_theme.html', {'this_theme': this_theme} )



def theme_delete(request, pk):
  mymodel = get_object_or_404(Themes, pk=pk)
  if request.method == 'POST':
    mymodel.delete()
    return redirect('themes/')  # Redirect to list view after deletion
  return render(request, 'themes_templates/delete_theme.html', {'object': mymodel})





# from django.shortcuts import render , redirect
# from .models import Themes

# def Themes_list(request):
#     themes = Themes.objects.all()
#     return render(request, 'themes_templates/home.html', {'themes': themes})



# def theme_detail(request , id ): 
#     theme_detail = Themes.objects.filter(pk=id)
#     return render(request, 'themes_templates/theme_detail.html', {'theme_detail': theme_detail}) 


# def theme_create(request):
#     if request.method == 'POST':
#         theme_name = request.POST['theme_name']
#         theme_detail = request.POST['theme_detail']
        
#         new_theme = Themes(theme_name=theme_name, theme_detail=theme_detail)
#         new_theme.save()
#         redirect('theme_detail'    )

#     else:
#         return render(request, 'themes_templates/add_theme.html')    