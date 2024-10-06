from django.db import models

class Post(models.Model):

    title = models.CharField(max_length=100)
    content=models.TextField()
    img_url= models.URLField(max_length=300,null=True)
    created_at =models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    