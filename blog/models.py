from django.db import models
from django.utils.text import slugify


class Post(models.Model):

    title = models.CharField(max_length=100)
    content=models.TextField()
    img_url= models.URLField(max_length=300,null=True)
    created_at =models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, null=True, blank=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    # def save(self, *args, **kwargs):
    # # Check if the slug is empty or needs to be updated
    #     if not self.slug:
    #         base_slug = slugify(self.title)
    #         slug = base_slug
    #         counter = 1
    #         # Ensure slug is unique by appending a number if necessary
    #         while Post.objects.filter(slug=slug).exists():
    #             slug = f"{base_slug}-{counter}"
    #             counter += 1
    #         self.slug = slug
    #     super().save(*args, **kwargs)


    def __str__(self):
        return self.title

    