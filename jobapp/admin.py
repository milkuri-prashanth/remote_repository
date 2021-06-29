from django.contrib import admin
from jobapp.models import hydjobs,bangjobs,chennijobs,punejobs

# Register your models here.
class hydjobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','addr','email','pno']
class bangjobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','addr','email','pno']
class chennijobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','addr','email','pno']
class punejobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','addr','email','pno']

admin.site.register(hydjobs,hydjobsAdmin)
admin.site.register(bangjobs,bangjobsAdmin)
admin.site.register(chennijobs,chennijobsAdmin)
admin.site.register(punejobs,punejobsAdmin)
