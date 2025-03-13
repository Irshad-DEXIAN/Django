from django.db import models 
from django.utils.text import slugify
from django.contrib.auth.models import User


# Category table
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Post table
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    img_url = models.ImageField(null=True, upload_to="posts/images")
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    is_published = models.BooleanField(default=False)

    def save(self ,*args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    @property
    def formatted_img_url(self):
        if self.img_url.__str__().startswith(('http://','https://')):
            url = self.img_url
        else:
            url = self.img_url.url
        return url

    def __str__(self):
        return self.title
    

# About table
class About(models.Model):
    content = models.TextField()

