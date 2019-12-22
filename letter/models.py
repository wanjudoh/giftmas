from django.db import models
from django.utils import timezone

# Create your models here.

class Letter(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=200)
    name = models.CharField(max_length=5)

    design = models.IntegerField(default=0)
    gift = models.IntegerField(default=0)
    receiver = models.CharField(max_length=100)
    sender = models.CharField(max_length=100)
    sentAt = models.DateTimeField(auto_now=True)

    def save(self, **kwargs):
        if not self.id:
            self.sentAt = timezone.now()
        super(Letter, self).save(**kwargs)
    
    class Meta:
        ordering = ['-sentAt']
    
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.content[:20]