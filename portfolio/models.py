from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class UserMeta(models.Model):
    name = models.CharField(max_length=300, unique=True)
    about = models.TextField()
    work_description = models.TextField()
    image = models.ImageField(null=True)
    email = models.EmailField()
    instagram = models.CharField(max_length=200)
    github = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "users"

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=300, unique=True)
    description = models.TextField()
    meta = models.TextField()

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=300)
    date_created = models.DateField(auto_now_add=True)
    slug = models.SlugField(blank=True, editable=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    thumbnail = models.ImageField(null=True)
    content = models.TextField()

    class Meta:
        verbose_name_plural = "posts"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)