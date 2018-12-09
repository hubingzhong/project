from django.contrib import admin
from webtest.models import Webcase,Webcasestep

class WbecasestepAdmin(admin.TabularInline):
    list_display = ['webcasename','webteststep','webtestobjname','webfindmethod','webevelement','weboptmethod'
                    'webfindmethod','webtestresule','create_time','id','webcase']
    model = Webcasestep
    extra = 1

class WebcaseAdmin(admin.ModelAdmin):
    list_display = ['webcasename','webtestresule','create_time','id']
    inlines = [WbecasestepAdmin]
admin.site.register(Webcase,WebcaseAdmin)