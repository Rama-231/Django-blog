from django.db import models

# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300)
    content = models.TextField()
    author = models.CharField(max_length=100)
    slug=models.CharField(max_length=100)
    tiemStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title + ' by ' + self.author
    