from django.db import models
from django.utils import timezone

class Gift(models.Model):
    id = models.IntegerField(default=0, primary_key=True)
    title = models.CharField(max_length=30)
    img = models.TextField()

    def __str__(self):
        return self.title

class Letter(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=1000)
    name = models.CharField(max_length=8)

    design = models.IntegerField(default=0)
    # gift = models.IntegerField(default=0)
    gift = models.ForeignKey(Gift, on_delete=models.CASCADE)
    #receiver = models.CharField(max_length=100)
    #sender = models.CharField(max_length=100)
    sentAt = models.DateTimeField(auto_now=True)
    #pw = models.CharField(default='0', max_length=4)
    # pw = models.CharField(null=True, max_length=4)

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
