from django.db import models
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField

# Create your models here.
class UserMeta(models.Model):
    name = models.CharField(max_length=300, unique=True)
    about = models.TextField()
    about_site = models.TextField(verbose_name="About Site")
    image = models.ImageField(null=True)
    resume = models.FileField(null=True)
    email = models.EmailField()
    instagram = models.CharField(max_length=200)
    github = models.CharField(max_length=200)
    linkedin = models.URLField()

    class Meta:
        verbose_name_plural = "users"

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=300, unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class Post(models.Model):
    slug = models.SlugField(blank=True, editable=False)
    title = models.CharField(max_length=300)
    date_created = models.DateField(auto_now_add=True)
    date = models.DateField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    thumbnail = models.ImageField(null=True)
    external_link = models.URLField(blank=True)
    content = RichTextField()

    class Meta:
        verbose_name_plural = "posts"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)