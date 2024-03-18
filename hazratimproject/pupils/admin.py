from django.contrib import admin

from pupils.models  import Pupils

# admin.site.register(Pupils)

class PupilAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullname' , 'mark1' , 'mark2' , 'mark3' , 'mark4' )
    search_fields = ('fullname', )
    list_filter = ('mark1','mark2','mark3','mark4' )
# Register your models here.

admin.site.register(Pupils , PupilAdmin )

 