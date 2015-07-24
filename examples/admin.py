from django.contrib import admin
from examples import models

class CommentInline(admin.TabularInline):
    model = models.Comment


class DocumentAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'added_by', None) is None:
            obj.added_by = request.user
        obj.last_modified_by = request.user
        obj.save()
    
    def queryset(self, request):
        qs = super(DocumentAdmin, self).queryset(request)

        # If super-user, show all comments
        if request.user.is_superuser:
            return qs
        
        return qs.filter(added_by=request.user)

    def change_view(self, request, object_id, form_url='',extra_context=None):
        result = super(DocumentAdmin, self).change_view(request, object_id,form_url, extra_context)
        document = models.Document.objects.get(id__exact=object_id)        
        if not request.POST.has_key('_addanother') and \
              not request.POST.has_key('_continue'):
            result['Location'] = document.get_absolute_url()
        return result

class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Document, DocumentAdmin)
admin.site.register(models.Comment, CommentAdmin)

"""
    def change_view(self, request, object_id, extra_context=None):
        result = super(DocumentAdmin, self).change_view(request, object_id, extra_context)
        document = models.Document.objects.get(id__exact=object_id)
        return result
        
        if not request.POST.has_key('_addanother') and \
              not request.POST.has_key('_continue'):
            result['Location'] = document.get_absolute_url()
        return result

"""