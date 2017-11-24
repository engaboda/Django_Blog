from django.contrib import admin

# Register your models here.
from posts.models import Posts

class PostModelAdmin(admin.ModelAdmin):
    list_display=["title","updated","timestamp"]
    list_editable=["title"]
    list_display_links=["updated"]
    list_filter = ["updated","timestamp"]
    search_fields=["title","content"]
    class meta:
        model=Posts

admin.site.register(Posts,PostModelAdmin)