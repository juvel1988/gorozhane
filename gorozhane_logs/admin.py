from django.contrib import admin

from gorozhane_logs.models import  Events, User
admin.site.register(User)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
admin.site.register(Events, PostAdmin)