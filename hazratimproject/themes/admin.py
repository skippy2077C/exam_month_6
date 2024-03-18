from django.contrib import admin

# Register your models here.

from themes.models import Themes 


class ThemeAdmin(admin.ModelAdmin):
    list_display = ('theme_name' , 'theme_detail')

admin.site.register(Themes, ThemeAdmin)


# class PupilAdmin(admin.ModelAdmin):
#     list_display = ('id', 'fullname' , 'mark1' , 'mark2' , 'mark3' , 'mark4' )
#     search_fields = ('fullname', )
#     list_filter = ('mark1','mark2','mark3','mark4' )
# # Register your models here.

# admin.site.register(Pupils , PupilAdmin )

 