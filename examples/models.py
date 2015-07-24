from django.db import models
from django.db.models import signals
from django.contrib.auth.models import User
from django.core.mail import send_mail

class Document(models.Model):
    '''A Document is a blog post or wiki entry with some text content'''
    name = models.CharField(max_length=255)
    text = models.TextField()
    added_by = models.ForeignKey(User, db_column='added_by_id', null=True, blank=True)

    
    def __unicode__(self):
        return self.name
    
    def get_absolute_url(self):
        return "/admin/examples/document/%s/" % self.id



class Comment(models.Model):
    '''A Comment is some text about a given Document'''
    document = models.ForeignKey(Document, related_name='comments')
    text = models.TextField()
    
def notify_admin(sender, instance, created, **kwargs):
    '''Notify the administrator that a new user has been added.'''
    return
    if created:
       subject = 'New user created'
       message = 'User %s was added' % instance.username
       from_addr = 'no-reply@example.com'
       recipient_list = ('admin@example.com',)
       send_mail(subject, message, from_addr, recipient_list)        

signals.post_save.connect(notify_admin, sender=User)    