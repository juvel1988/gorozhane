from django.contrib import admin

from gorozhane_logs.models import  Events, User, Culture, Architecture
admin.site.register(User)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
admin.site.register(Events, PostAdmin)
admin.site.register(Culture, PostAdmin)
admin.site.register(Architecture, PostAdmin)