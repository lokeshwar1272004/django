from django.contrib import admin
from .models import data
from .models import offer


class dataAdmin(admin.ModelAdmin):
    list_display = ('NAME','Stock','Price')

class offerAdmin(admin.ModelAdmin):
    list_display = ('code','discount')



admin.site.register(data, dataAdmin)
admin.site.register(offer, offerAdmin)







