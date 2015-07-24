from django import template
from examples import models

register = template.Library()

@register.inclusion_tag('comments.html')
def display_comments(document_id):
    document = models.Document.objects.get(id__exact=document_id)
    comments = models.Comment.objects.filter(document=document)[0:5]
    return { 'comments': comments }