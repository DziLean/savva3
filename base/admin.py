from django.contrib import admin
from .models import *
# Register your models here.
from django.utils.html import format_html


# View for admin page
class UrlAdmin(admin.ModelAdmin):
    readonly_fields=('title', 'status_code')
    list_display = ('title', 'link', 'tags','status_code')

    list_filter = ('many_tag','areas',)

    def link(self,obj):
        return format_html("<a target='_blank' href='{url}'>{url}</a>", url=obj.url)

    def tags(self,obj):
        x=''
        for a in obj.many_tag.all():
            x = x + a.name
        return x

class RelationshipInline(admin.TabularInline):
    model = Relationship
    extra = 1
    fk_name = "to_resource"


class ResourceAdmin(admin.ModelAdmin):
    inlines = (RelationshipInline,)

admin.site.register(Url, UrlAdmin)
admin.site.register(Tag)
admin.site.register(Area)
admin.site.register(Video, ResourceAdmin)
admin.site.register(Author)
admin.site.register(Book, ResourceAdmin)
admin.site.register(Resource)
admin.site.register(Theorem)
admin.site.register(Course)
admin.site.register(Link)
