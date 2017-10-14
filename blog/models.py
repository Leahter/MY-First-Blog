from django.db import models
from django.utils import timezone

class Post(models.Model):
    writer = models.ForeignKey("auth.User")
    title = models.CharField(max_length=200)
    writing = models.TextField()
    creating_date = models.DateTimeField(default=timezone.now)
    publishing_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.publishing_date = timezone.now()
        self.save()
    def _str_(self):
        return self.title
