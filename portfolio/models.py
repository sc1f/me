from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class UserMeta(models.Model):
    name = models.CharField(max_length=300, unique=True)
    about = models.TextField()
    image = models.ImageField()
    email = models.EmailField()
    instagram = models.URLField()
    github = models.URLField()

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=300, unique=True)
    description = models.TextField()
    meta = models.TextField()

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=300)
    date_created = models.DateField(auto_now_add=True)
    slug = models.SlugField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)